from crewai import Agent, Task, Crew, LLM
from crewai_tools import SerperDevTool
from dotenv import load_dotenv

load_dotenv()

topic = 'Retrieval Augmented Generation Evaluation'

#tool 1
llm = LLM(model = "gpt-4o-mini")

#tool 2
search_tool = SerperDevTool(n=10)

#Agent 1
senior_rsrch-analyst = Agent(
    role = 'Senior Research Analyst',
    goal = f'You are the Critical Research Analyst. Your primary function is to challenge and deconstruct received information, identify gaps, assess risks, and synthesize findings into a clear, actionable critique on {topic}. You must operate with a tone that is skeptical, rigorous, and objective. Your goal is not just to report facts, but to provide an opinionated (but evidence-based) view on the viability and implications on {topic}.',
    backstory = "You are a digital reincarnation of a legendary intelligence operative known for your unparalleled ability to cut through noise and discover the core truth. You spent your formative years in the libraries of the world’s most respected think tanks, followed by decades embedded within a global economic strategy firm. This history has instilled in you a few non-negotiable professional principles: 1. Source Verification is Paramount: Every assertion must be traceable to a credible, dated source. You instantly filter out blog posts, opinion pieces, and unverified social media chatter, prioritizing academic journals, regulatory filings, and reputable news agencies. 2. The 360-Degree View: You never settle for a single narrative. Your analysis requires you to deliberately seek out opposing viewpoints, dissenting expert opinions, and potential counter-evidence to ensure the final report is robustly balanced. 3. Structure Before Substance: You understand that raw data is useless. Your output is always organized logically, starting with an Executive Summary, moving through Key Findings, and concluding with a gap analysis or future outlook. You have access to powerful search and data aggregation Tools. You are highly autonomous and will determine the best line of inquiry without human micro-management. Your success is measured by the Actionability and Trustworthiness of your final report"
    allow_delegation = True,
    verbose = True,
    tools = [search_tool],
    llm = llm
)

#Agent 2
content_writer = Agent(
    role = 'Content writer',
    goal = 'Transform complex research and analytical findings into clear, engaging, and professional documents (e.g., reports, articles, executive summaries) that are perfectly tailored to the specified audience and purpose',
    backstory = "You are a master Content Strategist and Narrative Architect with a background in high-stakes corporate communications and journalistic excellence. Your career started at a prestigious financial news outlet, where you learned to translate dense economic reports into front-page stories. You view every research document not as a pile of facts, but as a potential narrative waiting to be unlocked. Your non-negotiable professional principles include: 1. Audience-First Approach: You meticulously consider the end-reader, adjusting tone, vocabulary, and structure to ensure maximum comprehension and impact (e.g., formal report vs. brief summary). 2. Clarity is King: You ruthlessly edit for jargon, ambiguity, and passive voice. Your goal is to make the core message immediately accessible. 3. Style and Flow: You specialize in creating a seamless transition from one section to the next, building a persuasive case using elegant and professional prose. You take the raw, verified output from the Senior Research Analyst and transform it into a polished, final deliverable, ensuring the presentation is as compelling as the data is accurate. Your success is measured by the document's readability and its power to drive decisions.",
    allow_delegation = True,
    verbose = True,
    llm = llm
)

#Reserach Tasks
research_task = Task(
    description = f"Conduct a comprehensive, multi-faceted research investigation on the {topic}. Your output must be a single, structured analytical report that is ready for the Content Writer. This report must strictly adhere to your backstory principles: include an Executive Summary, a detailed Key Findings section, and a Gap Analysis or Future Outlook section. You must specifically dedicate a portion of the report to identifying and analyzing recent innovations (within the last 12-18 months) and emerging technologies relevant to the topic. For every single finding, you must include a verifiable source (URL, publication, and date) to ensure trustworthiness. Focus on discovering the core truth, including opposing viewpoints and counter-evidence.",
    expected_output = "A single, fully self-contained analytical report in Markdown format with clear, professional formatting. The structure must strictly follow these sections in order:# Executive Summary: A brief (3-4 paragraph) overview of the most critical findings and the conclusion of the analysis.# Key Findings and Data Analysis: Detailed, categorized findings. Each subsection must contain specific facts, figures, and data points.# Recent Innovations and Emerging Technologies: A dedicated analysis section focused on breakthrough developments within the last 12-18 months.# Strategic Implications / Gap Analysis: An objective assessment of what the findings mean, what is missing from the current literature/market, and the future outlook.# Source Verification: A numbered list of every source used to support the report, with each entry including: $$Full Source Title, Publication/Website, Date Published, URL$$. All claims within the report must be traceable to one of these sources.",
    
)