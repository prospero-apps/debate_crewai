from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class DebateCrewai():
    """DebateCrewai crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def candidate(self) -> Agent:
        return Agent(
            config=self.agents_config['candidate'], 
            verbose=True
        )

    @agent
    def judge(self) -> Agent:
        return Agent(
            config=self.agents_config['judge'], 
            verbose=True
        )

    
    @task
    def support(self) -> Task:
        return Task(
            config=self.tasks_config['support'], 
        )

    @task
    def oppose(self) -> Task:
        return Task(
            config=self.tasks_config['oppose'], 
        )

    @task
    def decide(self) -> Task:
        return Task(
            config=self.tasks_config['decide'], 
        )

    @crew
    def crew(self) -> Crew:
        """Creates the DebateCrewai crew"""

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True
        )
