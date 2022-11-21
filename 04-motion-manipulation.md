# 4. Motion and Manipulation

```{admonition} Note
Page underconstruction
```


## Planning actions

Action action(<parameters>)
• PRECOND: <conditions that must be true to
apply this actions>
• EFFECTS: <conditions that become true or false
after executing the action>

Action Fly(p, from, to)
PRECOND: Plane(p) ∧ At(p, from) ∧ Airport(from) ∧ Airport(to)
EFFECT: ¬At(p, from) ∧ At(p, to))
• positive and negative literals in effects can be separated
into an add list and and delete list


## Motion Planning

• Task Planner can tell the robot discrete steps but
can’t say how to execute them
• Discrete actions must be turned into operations in a
continuous world
• Planning actions set goals and constraints,
something else must implement motor actions

### configuration space


