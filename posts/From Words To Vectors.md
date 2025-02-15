# From Words to Vectors: The Journey of Neural Word Embeddings
Justin Donaldson
2025-02-14

# What Are Embeddings?

Embeddings are numerical representations of objects (such as words,
sentences, or images) in a continuous vector space. These
representations capture semantic meaning, making it possible for
machines to understand and compare them.

``` mermaid
graph LR
    %% Main embedding concepts
    E[Embeddings] --> SE[Sentence Embeddings]
    E --> ME[Multi-Modal Embeddings]
    E --> DE[Document Embeddings]
    
    %% Media types
    MT[Media Types] --> T[Text]
    MT --> I[Images]
    MT --> A[Audio]
    MT --> V[Video]
    
    %% Embedding techniques for different media
    T --> TE[Text Embeddings]
    T --> SE
    I --> IE[Image Embeddings]
    A --> AE[Audio Embeddings]
    V --> VE[Video Embeddings]
    
    %% Relationships between embeddings
    TE --> ME
    IE --> ME
    AE --> ME
    VE --> ME
    
    %% Cross-modal connections
    ME --> CR[Cross-Modal Retrieval]
    ME --> MS[Multi-Modal Search]
    
    %% Properties
    style E fill:#f9f,stroke:#333
    style MT fill:#bbf,stroke:#333
    style ME fill:#bfb,stroke:#333
    style CR fill:#fbb,stroke:#333
    style MS fill:#fbb,stroke:#333
```

1.  The core concept of embeddings branches into three main types:

    - Sentence embeddings (specialized for text)
    - Multi-modal embeddings (can handle multiple types of media)
    - Document embeddings (for longer text)

2.  Different media types (text, images, audio, video) each have their
    own specialized embedding techniques

3.  All these individual embedding types can feed into multi-modal
    embeddings, which enable:

    - Cross-modal retrieval (finding related content across different
      media types)
    - Multi-modal search (searching across different types of media
      simultaneously)

``` mermaid
flowchart TD
    subgraph Input[Input Processing]
        T[Text Input] --> TOK[Tokenization]
        TOK --> VOC[Vocabulary Creation]
        VOC --> OHE[One-Hot Encoding]
    end

    subgraph Training[Training Process]
        OHE --> NNI[Neural Network Input Layer]
        NNI --> HID[Hidden Layer]
        HID --> CTX[Context Learning]
        
        subgraph Context[Context Window]
            CW[Sliding Window]
            TW[Target Word]
            SW[Surrounding Words]
        end
        
        CTX --> OPT[Optimization]
        OPT --> LSF[Loss Function]
        LSF --> BP[Backpropagation]
        BP --> UP[Update Weights]
    end

    subgraph Output[Embedding Result]
        UP --> WV[Word Vectors]
        WV --> VS[Vector Space]
        VS --> SIM[Semantic Similarities]
        
        SIM --> |Similar words cluster together| REL[Related Words]
        SIM --> |Vector arithmetic possible| ANA[Analogies]
        SIM --> |Distance measures similarity| DIS[Word Relationships]
    end

    style Input fill:#e1f3ff,stroke:#333
    style Training fill:#fff3e1,stroke:#333
    style Output fill:#e1ffe1,stroke:#333
```
