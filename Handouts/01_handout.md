
# Chapter 1: Introduction to Artificial Intelligence

## What is Artificial Intelligence?

Artificial Intelligence (AI) is a field with the goal of creating machines that can **solve problems that are challenging for humans**. These machines are often referred to as **intelligent agents**.

Intelligence itself is defined as the **ability to learn or understand or deal with new or trying situations** and the **ability to apply knowledge**. AI is about learning and needs to be about situations that are hard or new. To achieve this, AI needs reasoning.

There are different types of AI discussed:
*   **Narrow AI:** An intelligent agent designed to solve a **specific problem**. Examples include driving a car or playing chess. Most current applications fall into this category. A narrow AI agent very good at one task (like driving) cannot necessarily do another (like flying an airplane or playing chess).
*   **Artificial General Intelligence (AGI):** A hypothetical intelligent agent that can **understand or learn any intellectual task that human beings can**. It would be like a replacement for human intelligence.
*   **Artificial Superintelligence:** A hypothetical intelligent agent possessing **intelligence surpassing that of the brightest and most gifted human minds**.

As of the sources, AGI and Artificial Superintelligence have not yet been reached, but research is moving in that direction.

## Approaches to Achieving AI

The sources discuss four main ideas for how we could think about creating artificial intelligence:

1.  **Thinking like a human:** This approach involves understanding how the human brain works as an information processing machine. It requires scientific theories of brain function. This area is related to cognitive sciences. It might involve introspection, predicting human behavior, or examining neurological data. Note that artificial neural networks in machine learning do not work like the brain.
2.  **Acting like a human:** This approach focuses on creating a machine that is **outwardly indistinguishable from a human**. Alan Turing proposed the **Turing Test** in 1950 as a thought experiment to define what acting like a human means. Turing rejected the question "Can machines think?" in favor of this behavioral approach. The test involves a human interrogator trying to distinguish between a human and an AI system through conversation.

    *   **Capabilities needed for the Turing Test:** Passing the Turing Test would require capabilities that are still core AI areas today, including **Natural language processing** (for communication), **Knowledge representation** (to remember things), **Automated reasoning** (to solve puzzles), and **Machine learning** (to improve over time).
    *   **Turing's Prediction:** Turing predicted that by 2000, machines would fool 30% of human judges for five minutes. Current systems like ChatGPT (2023) are suggested to be doing at least that.

    *   **Criticisms of the Turing Test:**
        *   Some human behavior is **not intelligent**.
        *   Some intelligent behavior may **not be human**.
        *   Human observers may be **easy to fool**. Expectations play a large role. Humans tend to humanize things (anthropomorphic fallacy).
        *   It's possible to **imitate intelligence without intelligence**. Early chatbots like ELIZA (1964) used simple pattern matching to simulate conversation. The **Chinese Room Argument** (John Searle, 1980) is a thought experiment illustrating that following complicated rules might appear intelligent from the outside, even if there is no true understanding.
        *   From an engineering perspective, imitating a human is **not a good way to solve practical problems**. Useful intelligent agents can be created without trying to imitate humans.

3.  **Thinking rationally:** This means drawing sensible conclusions from facts, logic, and data. It involves data-driven decision-making. This approach might involve describing system rules using formal logic notation and applying them to data.

    *   **Limitations:** It's often hard to describe real-world problems purely with logic because the world isn't black and white. Making good decisions in an uncertain world is very difficult with logical rules. Rules can become impractical with too many conditions.

4.  **Acting rationally:** This means trying to achieve the **"best" outcome**. "Best" implies the need for **optimization**. The desirability of outcomes can be measured by the economic concept of **utility**. If there is uncertainty, the agent needs to maximize the **expected utility**.

    *   **Advantages of Optimization:** Generality (not limited to logical rules), Practicality (adaptable to many real-world problems), Well established (existing solvers/methods), Avoids philosophy and psychology in favor of a clearly defined objective.
    *   **Bounded rationality:** In practice, expected utility optimization is subject to the agent’s knowledge and computational constraints. The agent does the best it can with its available knowledge and resources.

**This course focuses on creating narrow AI agents that act rationally**. The goal is to create machines that act in a way to solve a specific hard problem that traditionally required human intelligence.

## Intelligent Agents

Intelligent agents are **machines that act rationally in their environment**.

Components of an intelligent agent:
*   They need to **communicate with the environment** using percepts (inputs from environment, e.g., via sensors) and actions (outputs that affect the environment, e.g., via actuators).
*   They need to **represent knowledge**, reason, and plan to achieve a desired outcome. Representing knowledge allows the agent to remember things. Planning is needed for complicated tasks.
*   **Learning from experience** to improve performance is an **optional** component.

**Examples:**
*   **Self-Driving Car:** Percepts include other cars, cyclists, people crossing the street. Action would be to slow down or stop the car. The objective is to reach the destination safely. Stopping to let people cross is a rational action to optimize this objective.
*   **Homework and LLMs:** Percept is your prompt. Action is creating the next most likely word, which is done word-by-word. The user's objective might be a useful answer, but the LLM's objective is likely to create text similar to its training data (e.g., other essays). This process of generating text word-by-word is very different from how humans might structure an essay.

## AI vs. Machine Learning

**Artificial Intelligence** is about **creating intelligent agents**. It involves many techniques and technologies like sensing (vision), robotics, natural language processing, knowledge representation, and planning.

**Machine Learning (ML)** is a **set of techniques used within AI**. It involves **learning from examples instead of being explicitly programmed**. ML reverses the idea of writing a program to produce an output; instead, it looks at data and tries to reverse engineer a program that could create that data. Common ML methods include supervised learning, unsupervised learning, and reinforcement learning (RL). **Deep Learning** is one popular technique used in these ML methods.

ML can be used in various parts of an intelligent agent, such as smart sensors (e.g., detecting objects in images), actuators (e.g., learning how to walk), and the agent's "brain" (e.g., learning optimal actions from percepts).

## The History of AI

Key milestones in AI history include:
*   **1943:** Introduction of **artificial neural networks**.
*   **1950:** **Turing Test** devised as a thought experiment.
*   **1955:** The name "Artificial Intelligence" was first used at a conference.
*   **1965:** ELIZA, an early chatbot using simple pattern matching, was devised.
*   **1974-1980: First AI Winter** - Development stalled.
*   **1980s:** **Expert systems** (logic-based AI) were researched, but often didn't work well due to the difficulty of representing the real world purely with logic.
*   **1987-1993: Second AI Winter**.
*   **1989:** Universal approximation theorem for artificial neural networks.
*   **2009:** Google's first self-driving cars were driving around.
*   **2011:** **NVIDIA GPUs** started being used for deep learning, providing enormous computational speedup.
*   **2017:** **Transformer architecture** and Large Language Models (LLMs) emerged.
*   **2022:** **Generative AI models** like DALL-E and ChatGPT gained prominence.

Recent successes in AI are attributed to the dominance of machine learning, faster computers and specialized hardware (GPUs), vast amounts of data (Internet, text, sensors) and storage (cloud), and new optimization methods like deep learning.

## AI Today

AI is used in many areas:
*   **Vision and Image Processing:** Operating at superhuman performance. Includes OCR (reading text), Face detection, Vehicle safety systems, Visual search, and Image generation (like DALL-E).
*   **Natural Language Processing (NLP):** Operating at or near superhuman performance. Includes Text-to-speech, Speech-to-text (for voice commands), Machine translation, and Text generation using Large Language Models (LLMs). While AI can create high-quality text, the question of whether it truly understands language is still elusive.
*   **Robotics:** Significant development has occurred. Examples include Mars rovers, robot soccer (RoboCup), autonomous vehicles (Self-driving cars), drones (including for war efforts), personal robotics, humanoid robots, and robotic pets. The DARPA Grand Challenge was influential in autonomous vehicles.

There is an interesting phenomenon called **Moravec's Paradox**, stating that it is comparatively easy to make computers perform at an adult level on tasks like intelligence tests or playing chess, but difficult or impossible to give them the skills of a one-year-old in perception and mobility. For example, a teenager learns to drive easily, but a truly self-driving car is still elusive despite years of effort.

The **AI Effect** describes how tasks are no longer considered to require much intelligence as soon as a machine gets good at them. Examples include calculation, chess, and learning. The ability to create art is questioned as a uniquely human task in light of AI's capabilities.

## AI Ethics & Safety

AI ethics and safety are a new frontier, involving commonly cited principles.

Principles for **companies and organizations** using AI:
*   **Ensure safety**.
*   **Limit harmful uses of AI**.
*   Establish **accountability** (e.g., liability for accidents).
*   **Avoid concentration of power** (Winner-takes-All scenario leading to companies more powerful than states).

Principles to **protect individuals**:
*   **Uphold human rights and values**.
*   Ensure **fairness** (Equal opportunity/impact) and reflect diversity/inclusion.
*   Provide **transparency** (Explanations to build trust, e.g., medical AI explaining decisions).
*   Respect **privacy** (Concerns about surveillance).
*   Contemplate implications for **employment** (Income and purpose).

Principles for **Governance**:
*   Acknowledge **legal/policy implications**.
*   Governments need to regulate AI. Global coordination is seen as needed.

**Regulations and Policies:**
*   The European Union's **General Data Protection Regulation (GDPR)** since 2016 included rules on automated individual decision-making (Art. 22), allowing individuals to contest decisions made solely by automated means and request a human review.
*   California's CCPA has similar implementations but was not modeled after GDPR.
*   In the United States, there have been attempts at regulation, and in 2021, some US tech companies even asked for regulation to gain certainty and use it as a shield against lawsuits.
*   A US White House Executive Order on AI development (14110) was issued in 2023, emphasizing safety, responsible innovation, and protecting rights, but it was revoked in January 2025.

### Fairness: Algorithmic Bias

**Algorithmic bias** describes systematic errors in a computer system that create unfair outcomes, favoring one group over others.
Types of bias:
*   **Pre-existing bias:** Social and institutional norms influence the design and training data choices. Example: Using historical hiring data for jobs historically held by one gender can lead to bias in job applicant screening AI.
*   **Technical bias:** Limitations of the program or computational power. Example: Using data that is easy to obtain but is biased.
*   **Emergent bias:** Bias arises when algorithms are used in new or unanticipated contexts beyond their original training purpose. Example: Using a large language model trained for one purpose to support job candidate selection.

### Types of AI Safety

AI safety aims to **prevent accidents, misuse, or other harmful consequences of AI**. This involves:
*   **AI Testing:** Testing the AI system's behavior.
*   **Monitoring AI:** Continuously monitoring the AI's performance.
*   **Adversarial robustness:** Preventing others from abusing the AI, for example, through injecting manipulative information.

Ensuring these aspects can be done through corporate self-regulation, private watchdogs, government action, or international treaties. A combination is likely needed. A potential concern is whether a superintelligent AI could circumvent testing and monitoring.

### AI Safety and Optimizers

Intelligent agents are **optimizers**. Challenges arise because the objectives and rules given to the agent by developers might not perfectly align with the developers' or users' goals (goal/reward alignment).

*   **Reward hacking:** The AI learns to exploit unintended side effects or loopholes to get a high score on its objective without actually solving the intended problem. This happens when objectives and rules are not watertight. It's like finding a glitch in a game for infinite lives. AI needs to follow social norms, which is hard to encode in objectives.
*   **Instrumental convergence:** All intelligent agents may pursue common subgoals to get better at reaching their primary objectives. An example subgoal is the need for more power or resources. The worry is that an intelligent agent might try to gain more resources, potentially taking them from humans, leading to scenarios like re-routing energy or building more chips. While full "rise of the machines" might be far off, alignment and reward hacking are real issues even with current systems.

## Outlook

AI is a technology on the verge of significant leaps, expected to have a **profound impact** on how we live and work, similar to electricity or the internet. We can expect **unprecedented gains in productivity** from better narrow AI. However, new technologies also present dangers and need to be regulated. This course introduces techniques to create simple intelligent agents focused on narrow AI that acts rationally.
```