# InsideOut Crew

InsideOut Crew is a multi-agent AI system inspired by the core emotions from the movie "Inside Out." Each agent represents a distinct emotional perspective—Joy, Sadness, Anger, Disgust, and Fear—working together to analyze topics and generate nuanced, emotionally diverse responses. The system also includes a Personality Analyst agent that profiles the user's emotional tendencies, ensuring that all outputs are tailored and context-aware.

**How it works:**

- The Personality Analyst agent reads the user's knowledge base and summarizes their dominant emotional traits.
- For any given topic, each emotion agent (Joy, Sadness, Anger, Disgust, Fear) generates a response from their unique perspective.
- The system can synthesize these perspectives to create an output that matches the user's emotional profile.

This approach enables:
- Deep personalization based on the user's emotional profile
- Multi-faceted analysis of any topic, considering optimism, empathy, advocacy, ethics, and caution
- Outputs that are actionable, emotionally aware, and contextually relevant

Below you'll find details on the agents and tasks that power the InsideOut Crew.

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/inflow_crewai/config/agents.yaml` to define your agents
- Modify `src/inflow_crewai/config/tasks.yaml` to define your tasks
- Modify `src/inflow_crewai/crew.py` to add your own logic, tools and specific args
- Modify `src/inflow_crewai/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the inflow-crewai Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Agents and Tasks Overview

### Agents

- **personality_analyst_agent** ("Personality Analyst"): Extracts the user's personality profile and dominant emotional leanings from the knowledge source. Specializes in psychological profiling and provides core emotional weights for synthesis.
- **joy_agent** ("Joyful Optimist"): Highlights positive, optimistic, and beneficial aspects of a topic. Embodies happiness and hope, focusing on opportunities and successes.
- **sadness_agent** ("Empathetic Reflecter"): Identifies challenges, concerns, and empathetic considerations. Acknowledges difficulties and the importance of compassion.
- **anger_agent** ("Assertive Advocate"): Pinpoints injustices, frustrations, and areas needing decisive action. Driven by fairness and justice.
- **disgust_agent** ("Ethical Guardian"): Flags undesirable, unappealing, or morally objectionable aspects. Ensures only what is ethical and acceptable is considered.
- **fear_agent** ("Cautious Planner"): Identifies dangers, risks, and worst-case scenarios. Advises caution and preparedness.

### Tasks

- **analyze_personality_task**: Reads the knowledge source to summarize the user's personality profile, focusing on emotional leanings (Joy, Sadness, Anger, Disgust, Fear). Output is a concise summary to guide response tone.
- **joy_response_task**: Analyzes a topic and generates a positive, optimistic response from Joy's perspective.
- **sadness_response_task**: Analyzes a topic and generates an empathetic, cautious response from Sadness's perspective.
- **anger_response_task**: Analyzes a topic and generates a critical, confrontational response from Anger's perspective.
- **disgust_response_task**: Analyzes a topic and generates a disapproving, critical response from Disgust's perspective.
- **fear_response_task**: Analyzes a topic and generates a cautious, risk-aware response from Fear's perspective.

These agents and tasks are defined in `src/inflow_crewai/config/agents.yaml` and `src/inflow_crewai/config/tasks.yaml`.

## Support

For support, questions, or feedback regarding the InflowCrewai Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
