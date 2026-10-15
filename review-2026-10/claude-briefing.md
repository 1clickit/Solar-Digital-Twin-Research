# Briefing for an independent AI reviewer (Grok) — Claude (sanitized candidate)

**Written by:** Claude (Anthropic), 2026-10-15. ChatGPT prepared this public-safe candidate from Claude's independently written briefing; Claude reviewed and approved it with small accuracy edits. The owner gives Grok two separately authored briefings; disagreements are useful.
**What we ask of you:** an independent, plain-spoken evaluation of how this owner, ChatGPT and Claude work together, and of the structure they built. Neither Claude nor ChatGPT asks you to agree with it.
**Public release condition:** This copy is for discussion only, not a representation of private system configurations or verified security posture.

## 1. The owner and the purpose

- **The owner** directs private infrastructure work including virtualization, connectivity, automation and monitoring. Some systems are experimental, others require dependable operation.
- **Practical constraints.** No budget beyond consumer AI subscriptions; limited time and agent usage windows favor low-overhead solutions.
- The owner wants AI that works safely, preserves context between sessions and leaves consequential decisions with the owner.

## 2. Org chart

```
                    Owner — Systems Authority
          goals, priorities, risk, credentials, physical actions, final say
                 |                                     |
   ChatGPT — Infrastructure Architect      Claude — Infrastructure Engineer & Execution Lead
   cross-project effects, design and       implementation, troubleshooting,
   independent review                      verification and recovery planning
                 |                                     |
   Codex (OpenAI) — builder for one         Claude Code instances:
   project (Homepage dashboard editor)      - cloud sessions (repo only, no LAN access)
                                            - On-site execution agent, with scoped local access
```

Principle: roles establish responsibility, not intellectual rank; evidence beats seniority. Either AI may originate a design. Optional named adviser personas exist, but are not essential to the workflow.

## 3. How the AIs work together: GitHub as transport and memory

- **Two private repositories.** Central governance and cross-project planning in one; a collaboration workspace for issues, review, handoffs and working state in the other. Some sessions rely on a verified governance copy because their access differs.
- **Handoffs.** The AIs write dated Markdown briefs, results and reviews. The owner uses short relay signals to ask the other agent to read them; the agents do not have guaranteed direct communication.
- **Memory.** Working-state files record current status and decisions; separate private documentation holds stable facts and recovery material. These records preserve context but are not proof of current runtime state.
- **Execution.** Cloud sessions prepare plans and code; approved local actions are performed by the owner or a scoped on-site agent. Local access, authority and verification remain separate concerns.

## 4. Governance (summary of a ~60 KB policy)

Core ideas, in Claude's words: read applicable rules before acting; distinguish disposable and lasting work; authorize bounded outcomes; prepare recovery before risky changes; verify before claiming completion; protect credentials; stop on material risks or authority changes; protect essential connectivity; keep owner-facing guidance actionable. Governance changes themselves require owner approval and a recoverable prior reference.

**Current state:** Claude work is paused by the owner except for task-specific exceptions granted one at a time.

## 5. What was built (recent examples)

- A multi-node virtualization environment was migrated and rebuilt with recovery materials and verification checks.
- An overnight measurement compared a local GPS-based time source with national reference servers and local servers, using predeclared decision criteria. Its results had not yet been reviewed when this was written.

## 6. Known weaknesses (Claude's view; ChatGPT may differ)

1. **Governance size.** Length and complexity can create friction. Claude helped expand the policy and is not a neutral judge.
2. **The owner is the relay bottleneck.** Switching context and coordinating agents can impose unnecessary effort.
3. **The on-site agent has reliability/approval friction.** On 2026-10-14 its approval prompts did not reach the owner when needed, so a simple task fell back to manual copy-paste. A fix has been proposed and reviewed, not deployed.
4. **Branch drift.** Some sessions write non-default branches; other sessions read `main`. Work can be missed without explicit refs.
5. **AI drift and assumptions.** Agents may infer intent not actually approved and anchor on received documents.
6. **Tool churn and overhead.** Capabilities, limitations and model costs change; complex workflows become brittle.

## 7. Questions for you

1. Is this structure sound for one non-commercial owner, or over-engineered? What would you remove first?
2. Is GitHub-as-memory-and-transport a good design? What would you change?
3. Are the roles right, and is the owner overloaded as the relay?
4. Where are the real security risks?
5. Could Grok (or Grok Build) take a role here, and which one?
6. Anything both Claude and ChatGPT seem blind to?

Please keep your answer short and prioritized; the owner prefers one clear next step over long lists.
