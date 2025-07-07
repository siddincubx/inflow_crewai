from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource
from typing import List
from crewai import LLM

llm = LLM(
    model="gemini/gemini-2.0-flash",
    temperature=0.7,
)
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class InsideOutCrew():
    """InsideOutCrew crew"""

    agents: List[BaseAgent]
    tasks: List[Task]
    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def joy_agent(self) -> Agent:
        # CrewAI will load the configuration from agents.yaml
        return Agent(
            config=self.agents_config['joy_agent'], # type: ignore
            llm=llm 
            )

    @agent
    def sadness_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['sadness_agent'], # type: ignore
            llm=llm
            ) 

    @agent
    def anger_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['anger_agent'], # type: ignore
            llm=llm
        )

    @agent
    def disgust_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['disgust_agent'], # type: ignore
            llm=llm
        )

    @agent
    def fear_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['fear_agent'], # type: ignore
            llm=llm
        )

    @agent
    def person_controller_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['person_controller_agent'], # type: ignore
            llm=llm
        )

    # Define your tasks using the @task decorator
    @task
    def joy_response_task(self) -> Task:
        return Task(
            config=self.tasks_config['joy_response_task'] # type: ignore
        )

    @task
    def sadness_response_task(self) -> Task:
        return Task(
            config=self.tasks_config['sadness_response_task'] # type: ignore
        )

    @task
    def anger_response_task(self) -> Task:
        return Task(
            config=self.tasks_config['anger_response_task'] # type: ignore
        )

    @task
    def disgust_response_task(self) -> Task:
        return Task(
            config=self.tasks_config['disgust_response_task'] # type: ignore
        )

    @task
    def fear_response_task(self) -> Task:
        return Task(
            config=self.tasks_config['fear_response_task'] # type: ignore
        )

    @task
    def synthesize_final_response(self) -> Task:
        return Task(
            config=self.tasks_config['synthesize_final_response'] # type: ignore
        )

    @crew
    def crew(self) -> Crew:
        # Load knowledge sources
        # CrewAI will automatically find files in the 'knowledge' directory.
        # You can explicitly define them or let CrewAI discover them.
        # For a single text file, placing it in 'knowledge/' is often enough.
        user_profile_knowledge = TextFileKnowledgeSource(
            file_paths=['user_preference.txt']
        )


        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential, # Important for synthesis to happen after emotional responses
            verbose=True,
            # Assign the knowledge sources to the entire crew
            # This makes the knowledge available to all agents
            knowledge_sources=[user_profile_knowledge]
        )
