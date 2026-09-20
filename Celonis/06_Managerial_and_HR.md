# 06: Culture, Values & Behavioral Interview

## 1. Celonis Core Cultural Values
To clear the final managerial and HR rounds, candidates must demonstrate authentic alignment with Celonis's four core organizational values:

1. **We Own It**: Take complete accountability from design to deployment. No excuses, no hand-waving. If something breaks in production, own the fix.
2. **Customer First**: Every algorithm, feature, and optimization must produce measurable business value for the enterprise client.
3. **Best Team Wins**: Radical collaboration over individual egos. Champion diverse perspectives and mentor peers.
4. **Always Moving Forward**: Relentless curiosity and continuous technical improvement.

---

## 2. Structured STAR Behavioral Answers for Adarsh Saurabh

### Question: "Tell me about a time you had to deal with a major technical setback or unexpected obstacle."
* **Situation**: During the **Hack4CG Hackathon**, our team was building a real-time facial emotion recognition pipeline. With 6 hours remaining before final evaluation, our inference model was consuming 98% GPU memory and dropping frames on live camera feeds.
* **Task**: As team lead, I had to ensure our prototype delivered smooth, sub-second inference on standard evaluation laptops without crashing.
* **Action**: I initiated a rapid profiling session and discovered our OpenCV video feed was maintaining uncompressed image buffers in memory. I restructured the capture pipeline using vectorized cropping and quantized the model weights, dropping memory consumption by 65% and boosting frame rates to 30 FPS.
* **Result**: We secured **Rank 1 out of 50+ competing teams**, and our project was praised for zero-latency live demonstration.

### Question: "Why Celonis over other software firms?"
* **Optimal Response**:
  > *"Celonis isn't just another enterprise SaaS company building standard CRUD forms; Celonis created the entire category of Process Mining and transformed how Global Fortune 500 companies execute. What excites me most as an engineer is the sheer scale and mathematical beauty of the problem: processing billions of unstructured ERP event logs, reconstructing directed graphs dynamically, and executing queries on custom columnar engines in sub-seconds. With my background in Computer Science and mathematical signal optimization, Celonis offers the perfect engineering crucible to solve deep systems challenges."*
