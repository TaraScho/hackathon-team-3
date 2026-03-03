Final presentation - 10 minutes per team share what you built and what you learned.

## What problem were we curious about?
- IaC → Datadog, automatically.
- Can Claude read an IaC repo and automatically stand up Datadog observability that matches the cloud resources it defines? 
- We were curious about configuring drift detection, custom dashboards, and other Datadog tools like workflows, app builder apps, monitors, etc.
- how can we go from repo + datadog api creds -> something cool in datadog.

## Live demo

### Introduce components 
- introduce stickerlandia -- briefly explain stickerlandia
- introduce app builder
- introduce worklows
- we all know dashboards, but did you know that app builder apps with workloads can be added to dashboards?

### "Demo" (Screenshot of claude working and live demo of finished product)
- A truly live demo will be difficult because the end to end process may take 10 minutes or longer to complete.
- Suggest we have either a recording/gif whatever sped up highlighting the cool part of the process and then live demo the end resulting dashboard(s) in our hackathon Datadog org

## What did we learn?
- Because of the way the Datadog documentation loads the Action Catalog action definitions and Workflow Automation/App Builder blueprints at run time, it is very hard to get these assets in an agent's context. 
- It is easy to build workflows and apps in the Datadog UI with Bits AI, but very difficult to do so with a local coding agent like Claude Code - even with very distinct prompting - the coding agents struggle to generalize from the examples provided.

## How AI helped or hurt?
- skip/callout in other parts of the presentation

## What AI tools did we use?
- Claude Code and skills

## Datadog usage and insights

We used
- Datadog public API
- Datadog Terraform provider
- Datadog Action Catalog
- Datadog Workflow Automation
- Datadog App Builder
- Datadog Dashboards
- Datadog AWS Integrations and resource scanning/Resource Catalog

## What we will do next
- Learn more about how action catalog specs are maintained and how to best work with them using coding agents
- Keep pursuing the IaC drift detection idea using some of the ideas we brainstormed but didn't have time to implement