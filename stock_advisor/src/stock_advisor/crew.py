from crewai import Agent, Crew, Process, Task

from crewai.project import CrewBase, agent, crew, task

from crewai.agents.agent_builder.base_agent import BaseAgent

from typing import List

from pydantic import BaseModel, Field

from crewai_tools import SerperDevTool

from .tools.push_notifications_tool import Push_Notification_Tool

from crewai.memory import ShortTermMemory, LongTermMemory, EntityMemory

from crewai.memory.storage import RAGStorage

from crewai.memory.storage.ltm_sqlite_storage import LTMSQLiteStorage


web_search_tool = SerperDevTool()

push_notifications_tool = Push_Notification_Tool()

class TrendingCompany(BaseModel):

    """The company or startup that has gained recognition via news"""

    company_name: str = Field(description= "Company name")

    company_ticker: str = Field(description = "Company stock symbol")

    reason: str = Field(description="Reason of coverage in the news")

class TrendingCompaniesList(BaseModel):

    """List of companies which are being covered in the news"""  

    companies_list: List[TrendingCompany] = Field(description= "List of companies covered in the news")

class TrendingCompanyResearch(BaseModel):

    """Detailed research output of the company""" 

    name: str = Field(description= "Company name")

    market_postion: str = Field(description="Current market position and competitive analysis")

    future_outlook: str = Field(description="Future outlook and growth prospects ")

    potential_investment: str = Field(description= "Scope and suitability for investment")

class TrendingCompaniesResearchList(BaseModel):

    """List of the companies researched"""

    researched_companies_list: List[TrendingCompanyResearch] = Field(description= "Comprehensive Research list of the trending companies")

@CrewBase
class StockAdvisor():
    """StockAdvisor crew"""

    agents_config = 'agents.yaml'

    tasks_config = 'tasks.yaml'

    
    @agent
    def company_researcher(self) -> Agent:
        return Agent(

            config=self.agents_config['company_researcher'],

            tools = [web_search_tool],

            memory = True
             
        )

    @agent
    def financial_researcher(self) -> Agent:
        return Agent(

            config=self.agents_config['financial_researcher'], 

            tools = [web_search_tool]
        )
    

    @agent
    def stock_advisor(self) -> Agent:

        return Agent(

            config=self.agents_config['stock_advisor'],

            tools = [push_notifications_tool], 
            
            memory = True
            
        )
    
    @agent
    def investment_manager(self) -> Agent:

        return Agent(

           config = self.agents_config['investment_manager'],

           verbose = True
        )
    

    
    @task
    def find_trending_companies(self) -> Task:

        return Task(

            config=self.tasks_config['find_trending_companies'],

            output_pydantic = TrendingCompaniesList
        )

    @task
    def research_trending_companies(self) -> Task:
        return Task(

            config=self.tasks_config['research_trending_companies'],

            output_pydantic = TrendingCompaniesResearchList

        )
    
    @task
    def filter_out_best_stock(self) -> Task:

        return Task(

            config = self.tasks_config['filer_out_best_stock'],

            output_pydantic = TrendingCompanyResearch
        )

    @crew
    def crew(self) -> Crew:

        investment_manager = Crew(

            config = self.agents_config['investment_manager'],

            allow_delegation = True
        )

        short_term_context = ShortTermMemory(

            context_storage = RAGStorage(

                embedder_config = {

                    'provider' : 'openai',

                    'config' : {

                        'model' : 'text-embedding-3-small'
                    }

                },
                type = "short-term",

                path = "./memory/"
            )
        )

        long_term_context = LongTermMemory(

            LTMSQLiteStorage(

                database_path = "./memory/long_term_storage.db"
            )
        )

        entity_context =  EntityMemory(

        entity_storage = RAGStorage(

                embedder_config ={

                "provider" : "openai",

                 "config" :  {

                    "model" : "text-embedding-3-small"

                 }
                 },
                 type = "short-term",

                 path = "./memory/"
            ),
        )

        

        return Crew(

            agents = self.agents,

            tasks = self.tasks,

            process = Process.hierarchical,

            verbose = True,

            manager_agent = investment_manager,

            memory = True,

            short_term_memory = short_term_context,

            long_term_memory = long_term_context,

            entity_memory = entity_context

        )
    