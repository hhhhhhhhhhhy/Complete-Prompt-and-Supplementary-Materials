# Evaluation Prompt:

Prompt = 
'''
You will receive a scientific figure (image) and its corresponding descriptive text. Your task is to evaluate their alignment and completeness using two metrics:

1. Relevance Score (0-10):
   - Assess how well the text describes and connects to the visual content of the figure
   - Consider: 
   - Accurate representation of data/patterns
   - Logical connection between textual explanations and visual elements
   - Appropriate referencing of figure components (axes, labels, annotations)
   - 0 = Completely unrelated/misleading
   - 10 = Perfect alignment with all elements addressed

2. Completeness Score (0-10):
   - Evaluate whether the text provides sufficient and comprehensive description of the figure
   - Consider:
   - Coverage of all key elements and features
   - Explanation of data trends/significance
   - Contextualization within research framework
   - 0 = Missing all critical information
   - 10 = Fully exhaustive description with insightful interpretation

Instructions:
- The figures are from academic publications (may contain complex visualizations, multi-panel diagrams, or technical annotations)
- The text should demonstrate both accurate observation and meaningful interpretation
- Consider academic rigor - penalize oversimplification of complex figures

Output Format:
```json
{
  "relevance": {
    "score": [0-10],
    "rationale": "concise analysis of alignment strengths/gaps"
  },
  "completeness": {
    "score": [0-10],
    "rationale": "brief evaluation of descriptive adequacy"
  }
}
'''