# Prompt-Response example of section 3.3:

Prompt = f'''
[CAPTION] {caption}

[VISUAL CONTEXTS]
{"\n".join(visual_context)}

Note: The figure is divided into a {M}x{N} grid. Coordinates (row,column) indicate text locations.
For example: (2,3) means 2nd row from top and 3rd column from left.

[INSTRUCTION]
Analyze how the visual elements support the caption and identify relevant paragraphs that:
1. Explain the methodology shown in the figure
2. Discuss the experimental results
3. Compare with other approaches
Provide paragraph numbers and key supporting sentences.
'''

# Response:
'''
Response:
{
  "analysis": "The visual contexts in the image collectively express the framework of the proposed ABPEM by illustrating the components and processes involved in the model. Region (1,1) describes the input modalities (audio and video) and their encoding into tokens, which aligns with the text's explanation of encoding inputs into tokens using modality-specific encoders. Region (1,2) details the attention mechanisms and the classifier network, which corresponds to the text's description of attention bootstrapping and principal entropy minimization. The spatial layout suggests a flow from input encoding to attention processing and classification, reflecting the hierarchical structure of the ABPEM framework.",
  "supporting_evidence": [
    "To solve this problem, we propose attention bootstrapping that promotes cross-attention scores using self-attention scores.",
    "The framework of the proposed ABPEM is illustrated in Figure 2. During test time, the input audio and video are encoded by EA and EB to obtain hidden space representations (i.e. tokens).",
    "Then, the tokens from different modalities are concatenated and a tunable layer is applied to generate queries, keys and values for each token, which are used for attention.",
    "The attention bootstrapping is used on the attention map that aligns the distributions of cross-and self-attention.",
    "Subsequently, the attended tokens are processed by layer normalization, the feed-forward network, and the classifier network to generate predicted probabilities p ∈ ∆C−1.",
    "Finally, principal entropy minimization takes top k reliable classes and computes the principal part of the entropy, which is part of the objective."
  ]
}
'''
