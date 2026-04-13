# Analysis: Why Andrej Karpathy Abandoned RAG (Claude Code x Obsidian)

## VIDEO METADATA

- **Title**: Why Andrej Karpathy Abandoned RAG (Claude Code x Obsidian)
- **Channel**: sayed.developer (@sayeddev)
- **Duration**: 12:57
- **Language**: English (auto-generated captions)
- **Upload date**: April 7, 2026
- **Caption type**: Auto-generated
- **Word count (transcript)**: ~1,900 words
- **Chapters**: None (single continuous video)
- **View count**: Not available in metadata
- **Like count**: 289
- **Comment count**: 33
- **Channel followers**: 5,100

---

## FULL CLEANED TRANSCRIPT

Despite Cloud Code being the best coding assistant in the world, people are still finding ways to really push the limits of it. What you are seeing here is my Instagram videos that I made organized in this graph view. For example, if I click on one entity here, you can see that it's Google Maps API. So, I talked in one of my videos about Google Maps API, but also you can see a lot of other entities and also some topics related for example to an API concept. This is one of the first videos I made. So, here you will see API application programming interface like the definition coverage in videos and some also links concept mock interview concept server, which is another video that I made. This is all created by Cloud Code in a technique that was mainly introduced by Andre Karpathy with who is an AI researcher and I will show you how to do this in just 5 minutes. So, to give you a bit of background, he posted on X where he says LLM knowledge bases and he's explaining

--- [00:01] ---

what he's finding really interesting and useful using LLMs like Cloud Code. So, he's saying something I'm finding very useful recently using LLMs to build personal knowledge bases for various topics of research interest. In this way, a large fraction of my recent token throughput is less less into manipulating code and more into manipulating knowledge stored as markdown and images. And this is exactly what we are doing here. I have my video scripts stored as markdown files. We will talk about it, but just to understand the concept behind this, it is mainly creating your own digital brain starting with the data ingest. You are indexing source documents like articles, papers, repos, or in my case my Instagram videos into raw directory, which is represented here in raw as you can see, and then letting the LLM incrementally compile wiki, which is just a collection of MD files in a directory structure and the wiki includes summaries of all the data in the raw directory, backlinks, and then categorizes data into concepts, writes articles about them, and link them together as we saw here. So, here you can also as we mentioned before, you can see some entities like here there is an entity called Cloudflare, which I mentioned Cloudflare in one of my videos, but also you see a lot of like concepts that are layered and are connected to each other. And this is like part one of this data ingestion and these are all based on the markdown files that I have in my raw directory. So, this is how it start. And then we're using Obsidian as the IDE, which is the front end where he can view the raw data as the compiled wiki and the derived visualizations. Important to know that the LLM writes all of the data of the wiki. I rarely touch it. So, what we need to understand from here is I like this analogy of the digital brain. If you're focused on content creation or if you're a student that is focused on research, you can really take all the resources that you find useful on the internet and then put them in the raw directory and let Cloud Code create this wiki for you out of the box and you don't need to touch anything and this wiki will be organized in MD files that are by nature connected in this way that we see in this graph. And Obsidian is just a tool that let us basically visualize all of this in a very nice way. And then he's talking about where things get interesting is that once your wiki is big enough, for example, his is 100 articles and 400 words, you can ask your LLM agent all kinds of complex questions against the wiki and it will go off, do the research because it has all like kind of this connections and backlinks and all in markdown files, which makes it really powerful. And he mentioned, I thought I had to reach out for some fancy rag, but the LLM has been pretty good about auto maintaining the index files and brief summaries of all the documents. And the output instead of getting answers in text terminal, I like to have markdown files for me or slideshows. You can use Marp, which is like a tool that make basically PowerPoint presentations. So, now I will show you exactly how to replicate this setup, but for your use case. Want to go to Obsidian and then create a new vault. So, you go to manage vaults, create a new vault. So, you will create a new vault and then browse location. I will put it in my workspace and I will call this research brain, which means that I want to have it at the as a digital brain where I basically put all the resources I have around certain research and then it will create automatically this wiki for me and then later I can query this and get really nice results. So, as you can see, we have an empty basically files in Obsidian. We have our graph view is very basic, the welcome and the create link, which you can see

--- [00:05] ---

here. And now what we want to do is we basically want to populate it, right? So, what we need for this is we need resources as articles, research articles, and we need Cloud Code. And to show you actually what is happening behind the scenes, I think it's a good idea to open this in Visual Studio Code. So, if I go to Visual Studio Code and I open folder and I go to my workspace and then I reach out for the research brain, I am able to see basically the Obsidian and the welcome exactly matching what we saw what we saw before. Andre said, I wanted to share a possible slightly improved version of the tweet and he shared with us a gist, which is basically the description of how this works. And then we can basically copy paste all of this and pass it to Cloud Code and let it basically create for us a wiki that we are interested in. So, if I copy all of this now and I go to Cloud Code and then instruct it of what exactly you want to do. So, I will hold the space to use the voice feature and explain to it what exactly I want to achieve. I want you to read Andre Karpathy's method on how to basically create a wiki and manage it and I want to focus on wiki that is around my research interest. So, I will throw in raw directory a lot of research papers or research sources and I want you to manage all of that for me in the Andre Karpathy's way as instructed above. And then I hit enter and then Cloud Code is going to basically replicate this setup that Andre Karpathy has created and will basically we will slowly start seeing the files getting created here. So, you see here we got the raw, which has the assets and we got the wiki and Cloud Code is working on the setup. But what I want you to understand here is really the focus is on getting resources from the internet or from wherever you want and really throw them into the raw directory without thinking about it and Cloud Code will be able to like reason around the context that is inside these and will basically create for you this a wiki that has different levels. You have analysis, concept, entities, and sources that are basically linked together and that are represented as nodes in this graph that we see here. So, here we have the overview and then we have the index and logs and we will talk about them just shortly. But once you are done, you are basically ready to take any source and put it in the raw and I will show you how Cloud Code will be able to do it. Here Cloud Code is explaining how to use it actually. Ingest, drop a paper article into the raw, use Obsidian web clipper for articles, and query ask me anything about your research and I'll I'll search the wiki and lint say lint the wiki and I'll health go and check for some stale information or some orphans or contradictions or gaps that are in your knowledge base and clear them once you say lint. It's like the code linter. So, now what we want to do is we want to go to Obsidian web clipper and add it. So, I already added to Obsidian web clipper. It's also free. You can just download it. And then I want to go to a research page that I like from Anthropic. Since the main reason from this wiki is basically to manage the digital brain of my own research. So, for example, I'm interested in this page around alignment faking in large language models. So, I will go to extensions and I will use Obsidian web clipper to do it. I have already set up place where to basically paste this in raw. So, I will add to Obsidian. I will open Obsidian and you will see exactly alignment faking in large language models is placed inside the raw. So, you can see that also the web clipper did a really good job in extracting the information from this web page including the images. So, this is actually really nice. After that, I can really now go to Cloud Code and say the following. So, I hold space and I say, "Hey, I placed one research paper in the raw directory. I want you to ingest it, please." And now Cloud Code will go ahead and read it and then reason around it and insert it in the wiki in this specific kind of style, which is like connections, concepts, entities, sources as you can see here. So, here you can see source alignment. I can see that it's connected to multiple things. It's connected to concept deceptive alignment, entity Redwood Research, entity Claude 3 Opus. So, we have also like different backlinks and so on, and

--- [00:10] ---

it's slowly like kind of building it up. Which is I think a really interesting. And you could imagine that if you want to build more on top of it, you could take more research papers and then use web clipper. So, here I can also do the same for this. I can use web clipper, Obsidian web clipper and add to Obsidian then and open and then is also added and then I can go back to Claude code and say, "Hey, I have added a new resource in the raw file. Please detect it and also ingest it in my wiki." And we will also see more and more build up of this small knowledge base or graph view that we see here. I think what's really important to mention here as while while this is really powerful and really interesting, I think it's still not scalable. Even Andre is was mentioning that he has only 100 articles. So, you could really imagine when we have like gigabytes of data that we want to query, rag is still the best option there. I also want to mention something really important around the index and the log that we need to know, that we need to understand. The wiki index is basically the catalog of all the pages in the wiki organized by type. So, here we have like the sources, the entities, the concepts and the analysis and every piece of them is small description of it. I think this is really important to note. And also regarding the log is the chronological record of all wiki operations. So, when you for example ingest a long running Claude for scientific computing and here ingested research for example, it really keeps the time when did you ingest that article and basically when you initialize. So, it's like from down up you see it. Wiki initialize. So, this is the first operation that was done. For example, ingest alignment faking in large language models, which is the first article that we ingested. I think index and log are really important to understand. And of course, we have the Claude that MD file that is describing what are we doing in this project for Claude to understand every time what it should do. So, here we have research brain LLM wiki schema. This is a personal research knowledge base following the LLM wiki pattern. So, you can tell of course that Claude will basically read this file on every session to understand what we basically did and how will it answer us and the knowledge that it has in this wiki. And it also has like instructions around the technique used by Andre that we pasted in the very first time we created all of this around like conventions, ingestion, querying, and linting, and index and log format. So, it's like a full description for Claude code every time it start a session to understand that hey, this is a digital brain. Now the user will query me against it and I have to answer it based on this specific structure that is built for. If you guys found this useful and helpful, consider subscribing to my channel and I'll see you next time.

---

## CHAPTER BREAKDOWN

Since this video has no official chapters, here are logical segments based on topic shifts:

### [00:00 – 00:55] Introduction & Overview
The presenter introduces the topic by showing his organized Instagram videos in a graph view, demonstrating how Cloud Code (Claude Code) has created connections between entities like Google Maps API and other concepts. He introduces Andrej Karpathy as the originator of this technique.

### [00:55 – 02:40] Karpathy's LLM Knowledge Base Concept
Explains Karpathy's X (Twitter) post about using LLMs to build personal knowledge bases. The key insight: shifting token throughput from manipulating code to manipulating knowledge stored as markdown and images. Introduces the "digital brain" concept with data ingest into a raw directory.

### [02:40 – 04:15] Wiki Structure and Obsidian Integration
Describes how the LLM incrementally compiles a wiki from the raw directory, creating summaries, backlinks, and categorizing data into concepts. Obsidian serves as the frontend IDE for viewing the compiled wiki and visualizations. The LLM writes all wiki data automatically.

### [04:15 – 06:40] Setup Tutorial: Creating Your Research Brain
Step-by-step tutorial on creating a new Obsidian vault called "research brain." Shows how to use Karpathy's gist instructions, copy them to Claude Code, and instruct it to replicate the setup for your research interests.

### [06:40 – 08:25] Wiki Architecture and Commands
Explains the wiki structure: analysis, concepts, entities, and sources as interconnected nodes. Introduces key commands: "ingest" for new papers, "query" for asking questions, and "lint" for checking stale information, orphans, contradictions, and gaps.

### [08:25 – 10:00] Practical Demonstration: Ingesting Research
Live demonstration using Obsidian Web Clipper to save an Anthropic article about "alignment faking in large language models" to the raw directory. Shows Claude Code ingesting the article and creating connections to concepts (deceptive alignment), entities (Redwood Research, Claude 3 Opus).

### [10:00 – 11:00] Scalability Limitations and RAG Comparison
Important caveat: while powerful, this approach is not scalable for large datasets. Karpathy himself only has ~100 articles. For gigabytes of data, RAG (Retrieval-Augmented Generation) remains the better option.

### [11:00 – 12:57] Index, Logs, and Claude.md Configuration
Explains the wiki index (catalog of all pages organized by type) and logs (chronological record of operations). The Claude.md file provides instructions to Claude Code about the wiki schema, conventions, and how to respond to queries.

---

## TOPIC MAP

| Topic | First Mention | Duration Covered | Depth |
|-------|--------------|-----------------|-------|
| Claude Code (Cloud Code) | 00:00 | Throughout | Deep-dive |
| Andrej Karpathy's technique | 00:49 | Throughout | Deep-dive |
| Graph view visualization | 00:11 | 00:11-00:15, 03:23-03:25 | Discussed |
| LLM knowledge bases | 00:59 | 00:59-01:25 | Deep-dive |
| Digital brain concept | 01:37 | 01:37-01:40, 02:58-03:00 | Discussed |
| Data ingestion (raw directory) | 01:40 | 01:40-02:00, 07:00-07:06 | Deep-dive |
| Wiki compilation | 01:57 | 01:57-02:15 | Discussed |
| Markdown files organization | 01:24 | 01:24-01:26, 03:17-03:23 | Discussed |
| Obsidian as IDE | 02:41 | 02:41-02:50, 04:20-04:25 | Deep-dive |
| Backlinks and connections | 02:06 | 02:06-02:15, 09:59-10:04 | Discussed |
| Token throughput shift | 01:17 | 01:17-01:26 | Surface mention |
| RAG (Retrieval-Augmented Generation) | 03:55 | 03:55-04:02, 10:57-11:00 | Discussed |
| Research vault setup | 04:20 | 04:20-04:55 | Deep-dive |
| Obsidian Web Clipper | 08:29 | 08:29-09:16 | Deep-dive |
| Alignment faking in LLMs | 08:46 | 08:46-09:16 | Surface mention |
| Wiki index structure | 11:03 | 11:03-11:20 | Discussed |
| Wiki logs (chronological) | 11:22 | 11:22-11:45 | Discussed |
| Claude.md configuration | 11:57 | 11:57-12:45 | Deep-dive |
| Lint command | 07:56 | 07:56-08:24 | Discussed |
| Scalability limitations | 10:49 | 10:49-11:00 | Discussed |

---

## KEY CLAIMS & FACTS

- **[00:00]** "Claude Code being the best coding assistant in the world" — presenter's opinion
- **[00:49]** Andrej Karpathy is an AI researcher who introduced this technique
- **[00:59]** Karpathy posted on X about "LLM knowledge bases"
- **[01:17]** Karpathy's claim: "a large fraction of my recent token throughput is less into manipulating code and more into manipulating knowledge stored as markdown and images"
- **[01:40]** The system indexes source documents like articles, papers, repos into a raw directory
- **[01:57]** The LLM incrementally compiles a wiki from the raw directory
- **[02:00]** Wiki is "just a collection of MD files in a directory structure"
- **[02:04]** Wiki includes summaries of all data, backlinks, and categorizes data into concepts
- **[02:51]** "The LLM writes all of the data of the wiki. I rarely touch it."
- **[03:37]** Karpathy's wiki has "100 articles and 400 words" (likely meant 400K words or similar)
- **[03:55]** Karpathy's quote: "I thought I had to reach out for some fancy rag, but the LLM has been pretty good about auto maintaining the index files"
- **[04:08]** Output preference: markdown files or slideshows (using Marp for PowerPoint-style presentations)
- **[07:17]** Wiki has different levels: analysis, concept, entities, and sources
- **[07:56]** "Lint" command checks for stale information, orphans, contradictions, or gaps
- **[08:34]** Obsidian Web Clipper is free
- **[09:53]** Example connections: source "alignment faking" connects to concept "deceptive alignment", entity "Redwood Research", entity "Claude 3 Opus"
- **[10:49]** "This is really powerful and really interesting, I think it's still not scalable"
- **[10:51]** "Even Andre is was mentioning that he has only 100 articles"
- **[10:57]** "When we have like gigabytes of data that we want to query, rag is still the best option there"
- **[11:05]** "The wiki index is basically the catalog of all the pages in the wiki organized by type"
- **[11:22]** "The log is the chronological record of all wiki operations"
- **[12:08]** Claude.md file describes the project for Claude to understand what to do on every session

---

## NOTABLE QUOTES

- **[00:00]** "Despite Cloud Code being the best coding assistant in the world, people are still finding ways to really push the limits of it."
- **[01:17]** "A large fraction of my recent token throughput is less less into manipulating code and more into manipulating knowledge stored as markdown and images." — Andrej Karpathy (quoted)
- **[01:37]** "It is mainly creating your own digital brain starting with the data ingest."
- **[02:51]** "The LLM writes all of the data of the wiki. I rarely touch it."
- **[03:55]** "I thought I had to reach out for some fancy rag, but the LLM has been pretty good about auto maintaining the index files and brief summaries of all the documents." — Andrej Karpathy (quoted)
- **[06:56]** "The focus is on getting resources from the internet or from wherever you want and really throw them into the raw directory without thinking about it."
- **[07:56]** "Lint the wiki and I'll health go and check for some stale information or some orphans or contradictions or gaps that are in your knowledge base and clear them once you say lint. It's like the code linter."
- **[10:49]** "I think it's still not scalable. Even Andre is was mentioning that he has only 100 articles."
- **[10:57]** "When we have like gigabytes of data that we want to query, rag is still the best option there."
- **[12:42]** "This is a digital brain. Now the user will query me against it and I have to answer it based on this specific structure that is built for."

---

## SPEAKER ANALYSIS

**Single Speaker**: The video features one presenter from the channel "sayed.developer" (@sayeddev).

**Role**: Tutorial creator and educator demonstrating a technical workflow.

**Speaking Style**:
- Conversational and instructional tone
- Uses screen recording to demonstrate concepts in real-time
- Frequently references visual elements ("as you can see here", "if I click on one entity")
- Explains concepts step-by-step with practical demonstrations

**Key Contributions**:
- Introduces Andrej Karpathy's LLM wiki technique to a broader audience
- Provides a complete walkthrough from setup to usage
- Demonstrates the workflow with actual tools (Obsidian, Claude Code, Web Clipper)
- Offers honest assessment of limitations (scalability concerns)

**Presentation Approach**:
- Starts with a visual demo of the end result (graph view)
- Explains the theoretical background (Karpathy's X post)
- Provides hands-on setup instructions
- Shows live ingestion of a research article
- Concludes with important caveats about scalability

---

## DETAILED SECTION ANALYSIS

### [00:00 – 00:55] Introduction & Overview

The video opens with a striking claim about Claude Code being "the best coding assistant in the world," immediately positioning the tool as powerful yet still being pushed to its limits by creative users. The presenter shows his own use case: organizing Instagram video content into a graph view where entities like "Google Maps API" become interconnected nodes.

This introduction serves multiple purposes: it demonstrates the end result viewers can achieve, establishes the presenter's credibility as someone actively using the system, and introduces the key concept of entity-based knowledge organization. The mention of "mock interview concept server" and other videos suggests this is part of a larger content ecosystem.

The segment concludes by crediting Andrej Karpathy as the originator of this technique, setting up the authority behind the method being demonstrated.

### [00:55 – 02:40] Karpathy's LLM Knowledge Base Concept

This section dives into the theoretical foundation by referencing Karpathy's X post about "LLM knowledge bases." The key insight presented is a paradigm shift: instead of using LLM token throughput primarily for code manipulation, redirect it toward knowledge manipulation stored as markdown and images.

The "digital brain" analogy is introduced here as a central metaphor that recurs throughout the video. The architecture is explained: source documents (articles, papers, repos, videos) go into a "raw directory," and the LLM incrementally compiles them into a wiki structure. This separation of concerns—raw input versus processed knowledge—is fundamental to understanding the system.

The presenter emphasizes that the wiki includes summaries, backlinks, and concept categorization, all automatically generated. This is positioned as a hands-off approach where "the LLM writes all of the data."

### [02:40 – 04:15] Wiki Structure and Obsidian Integration

Obsidian is introduced as the "IDE" or frontend for viewing the compiled wiki and visualizations. This is an important distinction: Obsidian doesn't create the knowledge structure; it displays what the LLM has created.

The presenter reiterates that he "rarely touches" the wiki content—the LLM handles everything. This automation is positioned as a key benefit for content creators and researchers who want to focus on gathering resources rather than organizing them.

Karpathy's quote about not needing "fancy rag" is significant—it positions this approach as an alternative to traditional RAG systems for certain use cases. The preference for markdown file outputs (or Marp slideshows) over terminal text answers reflects a desire for persistent, shareable knowledge artifacts.

### [04:15 – 06:40] Setup Tutorial: Creating Your Research Brain

This is the first hands-on tutorial segment. The presenter walks through creating a new Obsidian vault called "research brain," emphasizing the intentional naming to reflect its purpose as a digital brain for research.

The process involves:
1. Creating the vault in Obsidian
2. Opening it in Visual Studio Code to see the file structure
3. Using Karpathy's gist instructions
4. Passing those instructions to Claude Code

The voice feature demonstration (holding space to speak to Claude Code) shows a natural language interface for complex setup tasks. The instruction to Claude Code is specific: replicate Karpathy's setup for the presenter's research interests.

The visual feedback of files being created in real-time ("we got the raw, which has the assets and we got the wiki") provides concrete evidence of the system working.

### [06:40 – 08:25] Wiki Architecture and Commands

This section explains the internal structure of the wiki: four levels (analysis, concepts, entities, sources) that are interconnected and represented as nodes in the graph view. The index and logs are introduced as important metadata structures.

The command vocabulary is introduced:
- **Ingest**: Drop a paper/article into raw
- **Query**: Ask questions about research
- **Lint**: Check for stale information, orphans, contradictions, gaps

The "lint" command is particularly interesting—it's analogous to a code linter but for knowledge bases, automatically identifying quality issues in the knowledge structure.

### [08:25 – 10:00] Practical Demonstration: Ingesting Research

The presenter demonstrates the full ingestion workflow:
1. Uses Obsidian Web Clipper (noted as free) to save an Anthropic article about "alignment faking in large language models"
2. Shows the article saved to the raw directory with images preserved
3. Instructs Claude Code: "Hey, I placed one research paper in the raw directory. I want you to ingest it, please."
4. Claude Code reads, reasons, and inserts the content into the wiki

The result shows automatic connection creation: the source article connects to the concept "deceptive alignment," entities "Redwood Research" and "Claude 3 Opus." This demonstrates the system's ability to extract and link related concepts without manual intervention.

### [10:00 – 11:00] Scalability Limitations and RAG Comparison

This is a critical honesty moment in the video. Despite the impressive demonstration, the presenter acknowledges a key limitation: scalability. Karpathy himself reportedly has only ~100 articles in his wiki.

The comparison to RAG is important: for gigabytes of data, traditional RAG remains superior. This positions the LLM wiki approach as optimal for focused research domains (dozens to low hundreds of documents) rather than large-scale knowledge bases.

This segment adds credibility by not overselling the technique and helping viewers understand when to use this approach versus alternatives.

### [11:00 – 12:57] Index, Logs, and Claude.md Configuration

The final section explains the metadata structures that make the system work:

**Index**: A catalog of all wiki pages organized by type (sources, entities, concepts, analysis), each with a brief description. This enables efficient navigation and querying.

**Logs**: A chronological record of all wiki operations, showing when articles were ingested and when the wiki was initialized. This provides auditability and temporal context.

**Claude.md**: Perhaps the most important file—it's a schema document that tells Claude Code how to understand and interact with the wiki on every session. It includes:
- The LLM wiki pattern being followed
- Conventions for ingestion, querying, linting
- Index and log format specifications
- Instructions for how to respond to queries

This file is what makes the system persistent and consistent across sessions—Claude Code reads it every time to understand "this is a digital brain" and how to operate within its structure.

---

## SYNTHESIS

### Central Thesis
Andrej Karpathy's LLM wiki technique offers a powerful alternative to RAG for personal knowledge management by using Claude Code to automatically organize research materials into an interconnected wiki structure, viewable through Obsidian—optimal for focused research domains with up to ~100 documents.

### Recurring Themes
1. **Automation**: The LLM writes all wiki content; users rarely touch it
2. **Digital Brain**: The knowledge base as an extension of human cognition
3. **Markdown as Native Format**: Knowledge stored as interconnected .md files
4. **Separation of Concerns**: Raw input directory vs. compiled wiki output
5. **Graph-Based Visualization**: Obsidian's graph view showing entity relationships

### Internal Contradictions
- The transcript mentions Karpathy's wiki has "100 articles and 400 words" which seems inconsistent—likely meant 400K words or the presenter misspoke
- The video title suggests Karpathy "abandoned RAG," but the content clarifies RAG is still best for large-scale data—this is clickbait framing

### What's Missing
- No discussion of costs (API usage for frequent Claude Code interactions)
- No comparison to other personal knowledge management tools (Roam, Logseq, Notion AI)
- No security/privacy considerations for sensitive research
- No troubleshooting guidance for when the LLM mis-categorizes content

### Strongest Moments
- The live ingestion demonstration showing automatic connection creation (09:30-10:04)
- The honest scalability assessment (10:49-11:00)—adds significant credibility
- The Claude.md explanation (11:57-12:45)—reveals the "secret sauce" of persistence

### Weakest Moments
- The opening claim about Claude Code being "the best coding assistant" is unsubstantiated opinion
- Some technical details are glossed over (how exactly does the LLM determine connections?)
- The "400 words" figure is confusing and never clarified

---

*Analysis generated from auto-generated YouTube captions. Some transcription errors may be present (e.g., "Cloud Code" instead of "Claude Code").*
