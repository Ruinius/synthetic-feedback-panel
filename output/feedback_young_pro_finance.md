# Feedback: Young Professional — Finance (David Kim)

## Overall Impression

Bluefin presents a sophisticated vision for multi-agent AI orchestration. As someone who spends his day between Bloomberg Terminal, Excel models, and PowerPoint pitch books, the promise of automated multi-step workflows is intellectually appealing. But I'm going to evaluate this the way I'd evaluate any investment: what's the risk, what's the return, and can I actually use it?

## What I Liked

- **The "business-friendly outputs" claim is the most compelling feature.** The gap between AI output and client-ready deliverables is real. When ChatGPT gives me markdown, I still have to spend 30 minutes formatting it into a PowerPoint slide. If Bluefin can produce outputs in DOCX or directly in formats my team uses, that's a measurable time saving.
- **Cost-conscious model selection is smart capital allocation.** I think about ROI on everything. If the platform can route simpler queries to cheaper models and reserve expensive compute for complex reasoning, that's efficient resource allocation — exactly how I'd design it.
- **The presentation is exceptional.** The website is the most polished AI product site I've seen. In finance, presentation quality is a proxy for organizational quality. The team that built this clearly has high standards.
- **Sub-agent orchestration could solve real workflow problems.** The research → synthesis → formatting pipeline is something I do manually every week. If I could say "analyze these three earnings transcripts, extract key themes, and produce a formatted summary" and have it actually work? That's worth money.

## What Concerns Me

- **Compliance is the gating factor, and it's unaddressed.** I work at a bulge-bracket bank. I cannot use any external tool that touches client data, deal information, or anything materially non-public. Full stop. There are no exceptions. I've seen colleagues get compliance violations for less. Bluefin mentions "secure" and "on-prem" — but those words need to mean SOC 2 Type II, data residency guarantees, and integration with our existing enterprise security stack. Vague claims are worse than no claims because they suggest the team doesn't understand the bar.
- **Hallucination risk in a multi-agent chain is compounding, not additive.** In finance, a single wrong number in a model can be catastrophic. If Agent 1 produces a slightly off figure and Agent 2 builds on it, and Agent 3 formats it into a client-facing document — that's a liability, not a feature. How does Bluefin handle intermediate verification? Can I audit the chain? Are there confidence scores? The pitch is silent on this.
- **No mention of source attribution.** When I produce analysis, every number needs a source. "AI generated this" is not an acceptable citation. If Bluefin's agents are producing outputs, I need to see exactly where each data point came from. No sources, no trust.
- **"Democratized agent power" sounds like "your junior analyst but faster."** That's either the best pitch or the most dangerous one. Junior analysts make mistakes that get caught in review. Autonomous agents making mistakes at scale, faster, without the same review muscle memory? That's a risk multiplier.
- **Pricing opacity.** In banking, if I can't build a clear ROI model, I can't justify the spend. "Cost conscious" is not a price. I need per-agent-run pricing, enterprise volume discounts, and a way to project monthly costs based on my usage patterns.

## Questions I Need Answered Before I'd Even Trial This

1. Is the platform SOC 2 Type II certified? If not, what's the timeline?
2. Can it be deployed within our existing VPC / data perimeter?
3. Does every agent output include source attribution?
4. Can I set up human approval checkpoints between agent steps?
5. What's the audit trail? Can I reconstruct exactly what each agent did and why?
6. What happens to my data after a workflow completes? Is it retained? For how long?

## Use Cases (Personal / Non-Work Only)

To be clear: I cannot and would not use Bluefin for anything work-adjacent until it's firm-approved. But for personal use:

1. **CFA study automation.** "Read this curriculum chapter, generate practice questions, quiz me, and explain what I got wrong." Right now I do this manually with ChatGPT.
2. **Personal financial analysis.** "Analyze my portfolio allocation vs. my target, identify drift, and produce a rebalancing recommendation in a formatted report." I'd pay for this.
3. **Research synthesis for investment ideas.** "Pull together a summary of these three industry reports and highlight the key contrarian takeaways." This is what I use Perplexity for, but a multi-agent version could be more thorough.

## Suggestions

1. **Get SOC 2 certified and lead with it.** In finance, compliance isn't a feature — it's the entry ticket. Put your certifications, data handling policies, and deployment options on the homepage.
2. **Build source attribution into every agent output.** Every claim needs a footnote. This is non-negotiable for any analytical use case.
3. **Offer an enterprise preview program with compliance documentation.** Give firms like mine a way to evaluate the platform within our security perimeter. This is how you get from "cool tool" to "approved vendor."
4. **Show me the audit trail.** A dashboard that shows every agent step, input, output, and decision. Transparency builds trust, especially when the consequences of errors are high.
5. **Price it transparently.** Per-workflow, per-agent-run, or per-seat — whatever the model, publish it. Let me build the ROI case for my manager.

## Verdict

**5/10** — The vision is strong and the execution on the demo is exceptional. But in my world, the question isn't "is this cool?" — it's "can I use this without getting a compliance violation?" Right now, the answer is unclear, and unclear is the same as no. The moment Bluefin publishes SOC 2 certification, demonstrates source attribution, and shows me a human-in-the-loop workflow with a full audit trail, I'll take a meeting. Until then, this is a personal tool at best, and I already have ChatGPT Plus for that.

> In finance, "trust but verify" isn't a saying — it's a survival strategy. Bluefin needs to show me the verification layer before I can trust the agents.
