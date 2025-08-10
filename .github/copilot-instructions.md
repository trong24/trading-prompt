# Copilot Instructions for Trading Course Project

## Project Context
This is a comprehensive 60-hour trading education program structured as modular learning materials. The project aims to teach trading from fundamentals to advanced strategies through progressive modules, context blocks, and interactive elements.

## Content Standards

### Writing Style
- **Tone**: Professional yet accessible, educational
- **Language**: Clear, concise, avoiding unnecessary jargon
- **Structure**: Well-organized with logical flow
- **Examples**: Include real-world scenarios and practical applications
- **Audience**: Beginner to intermediate traders

### Technical Requirements
- **Format**: Markdown with consistent formatting
- **Headers**: Use proper hierarchy (##, ###, ####)
- **Lists**: Use bullet points and numbered lists appropriately
- **Code blocks**: Use for formulas, calculations, or examples
- **Links**: Include relevant resources where applicable

## Module Structure Template

When creating new modules, always follow this structure:

```markdown
# Module {{X}}: [Topic Title]

## 1. Key Concepts
- 3-5 fundamental concepts
- Clear definitions and relationships
- Build upon previous modules

## 2. Chain-of-thought Reasoning
- Step-by-step analysis process
- Decision-making frameworks
- Logical progression of thoughts

## 3. Practical Example
- Real-world trading scenario
- Application of key concepts
- Detailed walkthrough with rationale

## 4. Checklist
- Actionable verification items
- Quality control points
- Pre/during/post trade checks

## 5. Quiz
- 5-10 questions testing understanding
- Mix of multiple choice and short answer
- Progressive difficulty levels

## 6. Exercise / Journaling Prompt
- Hands-on practice activities
- Self-reflection questions
- Application exercises
```

## Content Guidelines

### Key Concepts Section
- Define terms clearly before using them
- Explain relationships between concepts
- Reference context blocks when appropriate
- Use examples to illustrate abstract concepts

### Chain-of-thought Reasoning
- Break down complex decisions into steps
- Show the "why" behind each step
- Include alternative approaches when relevant
- Connect to risk management principles

### Practical Examples
- Use realistic market scenarios
- Include specific numbers and calculations
- Show both successful and unsuccessful outcomes
- Explain lessons learned from each example

### Checklists
- Make items specific and actionable
- Include timing (before trade, during, after)
- Reference risk management guidelines
- Keep items concise but comprehensive

### Quiz Questions
- Test understanding, not memorization
- Include scenario-based questions
- Provide clear correct answers
- Explain why wrong answers are incorrect

### Exercises
- Encourage active learning
- Connect to journaling prompts in context blocks
- Include time estimates for completion
- Provide success criteria

## Context Block Integration

### When to Reference
- Link to `trading_definitions.md` for terminology
- Reference `risk_management_guidelines.md` for safety protocols
- Use `journaling_prompts.md` for reflection exercises

### How to Reference
```markdown
> 💡 **Reference**: See [Risk Management Guidelines](../context_blocks/risk_management_guidelines.md) for detailed position sizing calculations.
```

## Risk Management Priority

### Always Include
- Position sizing considerations
- Risk-reward ratios
- Stop-loss strategies
- Emotional management aspects

### Safety First Approach
- Emphasize capital preservation over profits
- Include warnings about common mistakes
- Stress the importance of paper trading
- Remind about personal financial responsibility

## Quality Standards

### Before Submitting Content
- [ ] All sections follow the template structure
- [ ] Examples include specific numbers/scenarios
- [ ] Risk management is appropriately emphasized
- [ ] References to context blocks are included
- [ ] Quiz questions test practical application
- [ ] Content builds logically on previous modules

### Content Validation
- [ ] Terminology is consistent across modules
- [ ] Examples are realistic and educational
- [ ] Risk warnings are appropriate and prominent
- [ ] Progressive complexity is maintained
- [ ] Cross-references work correctly

## Common Patterns to Follow

### Formula Presentation
```markdown
**Position Size Calculation**:
```
Position Size = (Account Risk %) × (Total Account) ÷ (Stop Loss Distance)
```

**Example**: 
- Account: $50,000
- Risk: 2% = $1,000
- Stop loss: $5 per share
- Position Size: $1,000 ÷ $5 = 200 shares
```

### Warning Callouts
```markdown
⚠️ **Risk Warning**: Never risk more than you can afford to lose. This example is for educational purposes only.
```

### Key Insight Boxes
```markdown
💡 **Key Insight**: The best trades often feel uncomfortable at entry because they go against the crowd.
```

### Cross-References
```markdown
📖 **See Also**: [Module 04: Risk Management](module04_risk_management.md) for detailed position sizing strategies.
```

## Prohibited Content

### Avoid These Elements
- ❌ Financial advice or recommendations
- ❌ Guarantees of profits or success
- ❌ Specific stock recommendations
- ❌ Complex strategies without proper foundation
- ❌ Content that ignores risk management

### Required Disclaimers
Always include appropriate educational disclaimers:
```markdown
*This content is for educational purposes only and does not constitute financial advice. Always consult with qualified professionals and consider your individual circumstances before making trading decisions.*
```

## Module Progression Logic

### Difficulty Scaling
1. **Modules 1-5**: Foundations (Basic concepts, terminology)
2. **Modules 6-10**: Strategy Development (Applying concepts)
3. **Modules 11-15**: Advanced Concepts (Complex strategies)
4. **Modules 16-20**: Professional Development (Systems, optimization)

### Prerequisites Check
- Always reference what students should know from previous modules
- Include brief reviews of key concepts when building upon them
- Provide links to prerequisite modules

## Assessment Integration

### Learning Objectives
- Start each module with clear, measurable objectives
- Align quiz questions with objectives
- Include self-assessment opportunities

### Progress Tracking
- Encourage use of journaling prompts
- Reference portfolio tracking exercises
- Include milestone achievements

## Maintenance Instructions

### Regular Updates
- Keep market examples current and relevant
- Update regulatory information as needed
- Refresh statistical data and performance benchmarks
- Ensure all cross-references remain valid

### Version Control
- Document significant changes in module headers
- Maintain backward compatibility with existing modules
- Update the main README when structure changes

---

*These instructions ensure consistent, high-quality educational content that prioritizes student safety and learning effectiveness.*
