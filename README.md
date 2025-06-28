<!DOCTYPE html>
<html lang="en">
<body>
  <h1>✅ Debug Log: blood_test_analyzer_debug</h1>

  <h2>📦 Install & Run</h2>
  <pre>
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
  </pre>
  
  <h2>1) Fix Agent Import Path</h2>
  <div class="fix">
    <strong>Before:</strong>
    <pre>from crewai.agents import Agent</pre>
    <strong>After:</strong>
    <pre>from crewai import Agent</pre>
    <p><em>Why:</em> Agent is exported from the top-level package, as per CrewAI docs.</p>
  </div>

  <h2>2) Correct SerperDevTool Import</h2>
  <div class="fix">
    <strong>Before:</strong>
    <pre>from crewai_tools.tools.serper_dev_tool import SerperDevTool</pre>
    <strong>After:</strong>
    <pre>from crewai_tools import SerperDevTool</pre>
    <p><em>Why:</em> The tool is directly exposed from the `crewai_tools` package.</p>
  </div>

  <h2>3) Initialize LLM Properly</h2>
  <div class="fix">
    <strong>Added Imports & Init:</strong>
    <pre>
from crewai import Agent, LLM
llm = LLM(model="ollama/llama3.2", base_url="http://localhost:11434")
    </pre>
    <p><em>Why:</em> CrewAI v0.63+ requires explicit `LLM` initialization to connect models properly.</p>
  </div>

  <h2>4) Update PDF Loader Import</h2>
  <div class="fix">
    <strong>Before:</strong>
    <pre>from langchain.document_loaders import PDFLoader</pre>
    <strong>After:</strong>
    <pre>from langchain_community.document_loaders import PyPDFLoader</pre>
    <p><em>Why:</em> The previous loader was deprecated. `PyPDFLoader` from `langchain_community` is the current recommended class :contentReference[oaicite:1]{index=1}.</p>
  </div>

  <h2>5) Pydantic ValidationError: tools.0 not instance of BaseTool</h2>
  <p><em>Fix:</em> Subclass `BaseTool`, define `_run()`, and pass its instance (`blood_tool`) to Task instead of method/coroutine. CrewAI requires a `BaseTool` instance.</p>

  <h2>6) ImportError for BaseTool</h2>
  <p><em>Fix:</em> Change to <code>from crewai.tools import BaseTool</code>—that’s where it’s exported from.</p>

  <h2>7) ClassVar AttributeError</h2>
  <p><em>Fix:</em> Use instance attributes rather than `ClassVar`, e.g.:</p>
  <pre>
name: str = "blood_test_report_tool"
description: str = "Load text from blood test PDF"
  </pre>
  <p><em>Why:</em> CrewAI dynamically updates description on instances.</p>

  <h2>8) `PDFLoader` Undefined</h2>
  <p><em>Fix:</em> Add appropriate import:</p>
  <pre>from langchain_community.document_loaders import PyPDFLoader</pre>

  <h2>9) `ValueError: File path not valid`</h2>
  <p><em>Fixes:</em> Convert to absolute path, wrap Windows paths with <code>r"C:\..."</code>, and add existence checks before loading.</p>

  <h2>10) `TypeError: 'PyPDFLoader' object is not iterable`</h2>
  <p><em>Fix:</em> Use <code>docs = loader.load()</code> and then iterate through `docs`, not the loader itself.</p>

  <h2>11) Coroutines in `tools=[…]`</h2>
  <p><em>Fix:</em> All logic moved into sync `_run()` in `BaseTool`. `Task.tools` no longer includes async coroutines.</p>

  <h2>12) Agent Tools Passed Incorrectly</h2>
  <p><em>Fix:</em> Pass `BloodTestReportTool()`—not its method—to `tools=[ … ]`. CrewAI requires a proper tool instance.</p>

</body>
</html>
