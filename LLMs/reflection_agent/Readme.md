## Reflection Agents for Twitter Generation post.

a reflection agen is an AI system designed to act as an autonomous evaluator and editor its own output(retrieval/answers), employing a "Think-> Do -> Evaluate -> Improve" cycle rather than a single-pass "generate and forget" approach.

# Dependencies:

```bash
    poetry init # isntall env and python with dependencies managed.
    poetry add loaddot langchain-core langgraph black sort
```

# Running

```bash
    poetry run python main.py
```

## Diagrama StateGraph

```mermaid
graph TD
    %% Nodos
    START([__start__])
    GENERATE(generate)
    REFLECT(reflect)
    END([__end__])

    %% Conexiones
    START --> GENERATE
    GENERATE -.-> REFLECT
    GENERATE -.-> END
    REFLECT --> GENERATE

    %% Estilos para parecerse a la imagen
    style START fill:#f7d1b1,stroke:#333
    style GENERATE fill:#f2c2d4,stroke:#333
    style REFLECT fill:#f2c2d4,stroke:#333
    style END fill:#b9f2c1,stroke:#333
```
