# mod_python.py - Python Internals, GIL & Concurrency Module Generator

def get_content():
    toc = [
        ("rapid-recall", "⚡ 10-Min Rapid Recall Sheet"),
        ("visual-diagrams", "📊 Visual GIL & Garbage Collection"),
        ("core-deep-dives", "🧠 GIL Mechanics, Memory & AsyncIO"),
        ("interview-traps", "⚠️ High-Frequency Python Traps"),
        ("flashcards", "🎯 10 High-Frequency GFG Interview Q&As")
    ]

    # SVG 1: CPython GIL Execution Flow
    svg_gil = """
    <svg viewBox="0 0 860 300" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="py-arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8" />
        </marker>
        <marker id="py-green" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#34d399" />
        </marker>
      </defs>

      <!-- Thread 1 Timeline -->
      <text x="30" y="80" fill="#38bdf8" font-size="12" font-weight="800">Thread 1</text>
      <rect x="110" y="60" width="180" height="35" rx="4" fill="#0284c7" />
      <text x="200" y="82" fill="#ffffff" font-size="10" font-weight="700" text-anchor="middle">Holds GIL: Executing Python Bytecode</text>

      <rect x="295" y="60" width="120" height="35" rx="4" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5" />
      <text x="355" y="82" fill="#f43f5e" font-size="10" font-weight="700" text-anchor="middle">Blocked (Waiting)</text>

      <rect x="420" y="60" width="220" height="35" rx="4" fill="#065f46" stroke="#34d399" stroke-width="1.5" />
      <text x="530" y="82" fill="#34d399" font-size="10" font-weight="700" text-anchor="middle">I/O Operation (Releases GIL!)</text>

      <!-- Thread 2 Timeline -->
      <text x="30" y="150" fill="#34d399" font-size="12" font-weight="800">Thread 2</text>
      <rect x="110" y="130" width="180" height="35" rx="4" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5" />
      <text x="200" y="152" fill="#f43f5e" font-size="10" font-weight="700" text-anchor="middle">Blocked (Waiting for GIL)</text>

      <rect x="295" y="130" width="120" height="35" rx="4" fill="#059669" />
      <text x="355" y="152" fill="#ffffff" font-size="10" font-weight="700" text-anchor="middle">Acquires GIL &amp; Runs</text>

      <rect x="420" y="130" width="220" height="35" rx="4" fill="#059669" />
      <text x="530" y="152" fill="#ffffff" font-size="10" font-weight="700" text-anchor="middle">Holds GIL: Executing Bytecode</text>

      <!-- GIL Box Center -->
      <rect x="680" y="60" width="150" height="105" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="2" />
      <text x="755" y="90" fill="#fbbf24" font-size="12" font-weight="800" text-anchor="middle">GIL Mutex</text>
      <text x="755" y="110" fill="#fde68a" font-size="9" text-anchor="middle">Only 1 OS Thread</text>
      <text x="755" y="125" fill="#fde68a" font-size="9" text-anchor="middle">evaluates bytecode</text>
      <text x="755" y="145" fill="#94a3b8" font-size="8" text-anchor="middle">Switch interval: 5ms</text>

      <!-- Rule Callout at Bottom -->
      <rect x="50" y="210" width="760" height="60" rx="6" fill="#0f172a" stroke="#334155" />
      <text x="430" y="235" fill="#38bdf8" font-size="11" font-weight="700" text-anchor="middle">The Golden Python Concurrency Rule:</text>
      <text x="430" y="255" fill="#f1f5f9" font-size="10" text-anchor="middle">I/O-Bound Tasks &rarr; threading / asyncio (GIL released during socket/file wait) &nbsp;|&nbsp; CPU-Bound Tasks &rarr; multiprocessing (Bypasses GIL via separate processes)</text>
    </svg>
    """

    # SVG 2: Python Generational Garbage Collector
    svg_gc = """
    <svg viewBox="0 0 860 220" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="gc-arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#34d399" />
        </marker>
      </defs>

      <!-- Gen 0 -->
      <rect x="30" y="40" width="220" height="120" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2" />
      <rect x="30" y="40" width="220" height="28" rx="8" fill="#0369a1" />
      <text x="140" y="60" fill="#ffffff" font-size="11" font-weight="800" text-anchor="middle">Generation 0 (Youngest)</text>
      <text x="45" y="90" fill="#f1f5f9" font-size="10">• All newly created objects</text>
      <text x="45" y="110" fill="#94a3b8" font-size="9">• Scanned frequently (threshold: 700)</text>
      <text x="45" y="130" fill="#a7f3d0" font-size="9">• Survivors promoted to Gen 1 &rarr;</text>

      <line x1="250" y1="100" x2="305" y2="100" stroke="#34d399" stroke-width="2" marker-end="url(#gc-arrow)" />

      <!-- Gen 1 -->
      <rect x="315" y="40" width="220" height="120" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="2" />
      <rect x="315" y="40" width="220" height="28" rx="8" fill="#065f46" />
      <text x="425" y="60" fill="#ffffff" font-size="11" font-weight="800" text-anchor="middle">Generation 1 (Intermediate)</text>
      <text x="330" y="90" fill="#f1f5f9" font-size="10">• Survived Gen 0 collections</text>
      <text x="330" y="110" fill="#94a3b8" font-size="9">• Scanned after 10 Gen 0 runs</text>
      <text x="330" y="130" fill="#fde68a" font-size="9">• Survivors promoted to Gen 2 &rarr;</text>

      <line x1="535" y1="100" x2="590" y2="100" stroke="#34d399" stroke-width="2" marker-end="url(#gc-arrow)" />

      <!-- Gen 2 -->
      <rect x="600" y="40" width="230" height="120" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="2" />
      <rect x="600" y="40" width="230" height="28" rx="8" fill="#78350f" />
      <text x="715" y="60" fill="#ffffff" font-size="11" font-weight="800" text-anchor="middle">Generation 2 (Oldest / Long-Lived)</text>
      <text x="615" y="90" fill="#f1f5f9" font-size="10">• Modules, globals, singletons</text>
      <text x="615" y="110" fill="#94a3b8" font-size="9">• Scanned rarest (threshold: 10 Gen 1)</text>
      <text x="615" y="130" fill="#f87171" font-size="9">• Full cyclic GC collection pass!</text>

      <text x="430" y="195" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">CPython Tri-Generational Cyclic Garbage Collection (Weak Generational Hypothesis: Most objects die young!)</text>
    </svg>
    """

    content = r"""
    <!-- SECTION 1: RAPID RECALL -->
    <section id="rapid-recall" class="section-block">
      <div class="section-head">
        <h2 class="section-title">⚡ 10-Minute Rapid Recall Cheat Sheet</h2>
        <span class="pill pill-emerald">Python Under The Hood</span>
      </div>

      <!-- Concurrency Comparison Table -->
      <h3 style="font-size: 1rem; color: var(--accent-emerald); margin: 1rem 0 0.5rem;">1. Python Concurrency Models: Threading vs Multiprocessing vs AsyncIO</h3>
      <div class="table-container">
        <table class="dense-table">
          <thead>
            <tr>
              <th>Model</th>
              <th>Underlying Primitive</th>
              <th>Subject to GIL?</th>
              <th>Ideal Workload</th>
              <th>Memory &amp; Context Switch Cost</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>threading</strong></td>
              <td>Real OS Threads (POSIX threads)</td>
              <td><strong>YES</strong> (Only 1 thread runs Python code at a time).</td>
              <td>I/O-bound tasks (network requests, DB queries, reading files).</td>
              <td>Low memory (~8MB stack per thread); OS context switches.</td>
            </tr>
            <tr>
              <td><strong>multiprocessing</strong></td>
              <td>Separate OS Processes via <code>fork()</code> / <code>spawn</code></td>
              <td><strong>NO</strong> (Each process has its own independent Python interpreter and GIL!).</td>
              <td><strong>CPU-bound heavy compute</strong> (ML data prep, image processing, cryptography).</td>
              <td>High memory (duplicates process memory); IPC serialization overhead via <code>pickle</code>.</td>
            </tr>
            <tr>
              <td><strong>asyncio</strong></td>
              <td>Single-threaded Event Loop + Coroutines</td>
              <td>N/A (Single-threaded cooperative multitasking).</td>
              <td>High-concurrency network servers (10,000+ simultaneous open sockets).</td>
              <td><strong>Extremely lightweight (&lt; 1KB per coroutine)</strong>; zero OS context switches!</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Dunder Methods Cheat Sheet -->
      <h3 style="font-size: 1rem; color: var(--accent-blue); margin: 1.5rem 0 0.5rem;">2. High-Frequency Python Dunder (Magic) Methods</h3>
      <div class="table-container">
        <table class="dense-table">
          <thead>
            <tr>
              <th>Dunder Method</th>
              <th>When It Triggers</th>
              <th>Interview Trap / Note</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><code>__new__(cls, ...)</code></td>
              <td>Creates and returns the new instance memory before initialization.</td>
              <td>Called <em>before</em> <code>__init__</code>; used for Singletons and subclassing immutable types (<code>int</code>, <code>tuple</code>).</td>
            </tr>
            <tr>
              <td><code>__init__(self, ...)</code></td>
              <td>Initializes instance attributes after creation.</td>
              <td>Must return <code>None</code>; cannot create the object itself.</td>
            </tr>
            <tr>
              <td><code>__call__(self, ...)</code></td>
              <td>Enables instance to be invoked as a function: <code>obj()</code>.</td>
              <td>Used in custom Decorators, Neural network layers (PyTorch <code>nn.Module</code>).</td>
            </tr>
            <tr>
              <td><code>__enter__</code> &amp; <code>__exit__</code></td>
              <td>Context Manager protocol (<code>with open(...) as f:</code>).</td>
              <td><code>__exit__</code> catches exceptions and guarantees resource cleanup even on error!</td>
            </tr>
            <tr>
              <td><code>__slots__</code></td>
              <td>Explicitly declares allowed instance attributes as a tuple.</td>
              <td><strong>Eliminates <code>__dict__</code> overhead</strong>, saving 40-50% memory per object!</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- SECTION 2: VISUAL DIAGRAMS -->
    <section id="visual-diagrams" class="section-block">
      <div class="section-head">
        <h2 class="section-title">📊 Visual GIL & Garbage Collection</h2>
        <span class="pill pill-emerald">CPython Internals</span>
      </div>

      <div class="svg-diagram-card">
        __SVG_GIL_EXECUTION__
        <div class="diagram-caption">Figure 12.1: CPython GIL (Global Interpreter Lock) Execution Model — Demonstrating GIL Release during I/O Sycalls vs CPU Contention.</div>
      </div>

      <div class="svg-diagram-card">
        __SVG_GENERATIONAL_GC__
        <div class="diagram-caption">Figure 12.2: CPython Tri-Generational Cyclic Garbage Collection Flowchart (Generations 0, 1, and 2 Thresholds).</div>
      </div>
    </section>

    <!-- SECTION 3: CORE DEEP DIVES -->
    <section id="core-deep-dives" class="section-block">
      <div class="section-head">
        <h2 class="section-title">🧠 GIL Mechanics, Memory & AsyncIO</h2>
        <span class="pill pill-purple">Advanced Python</span>
      </div>

      <!-- Memory Management & Ref Counting -->
      <h3 style="color: var(--accent-emerald); font-size: 1.1rem; margin-top: 1rem;">1. CPython Memory Architecture: PyObject Header & Reference Counting</h3>
      <p style="color: var(--text-secondary); margin-bottom: 0.5rem;">
        Every single object in Python is wrapped in a C structure called <code>PyObject</code>:
      </p>
      <pre><code class="language-c">// CPython PyObject Definition (Include/object.h)
struct _object {
    _PyObject_HEAD_EXTRA // Doubly linked list for GC tracking
    Py_ssize_t ob_refcnt; // 64-bit reference counter
    struct _typeobject *ob_type; // Pointer to type descriptor (int, dict, etc.)
};</code></pre>
      <ul style="margin-left: 1.25rem; color: var(--text-secondary); line-height: 1.7;">
        <li><strong>Reference Counting ($O(1)$ Instant Cleanup):</strong> Whenever an object is referenced (assignment, passed to function), <code>ob_refcnt</code> increments. When reference falls out of scope, <code>ob_refcnt</code> decrements. When it hits $0$, memory is immediately returned to Python's memory pool (<code>PyMalloc</code>).</li>
        <li><strong>Cyclic Garbage Collector:</strong> Reference counting cannot detect circular references (e.g. <code>a.b = b; b.a = a</code>). Python uses a generational cyclic collector that finds unreachable reference cycles by isolating pointer references across tracking lists.</li>
      </ul>

      <!-- AsyncIO Event Loop -->
      <h3 style="color: var(--accent-blue); font-size: 1.1rem; margin-top: 1.5rem;">2. How AsyncIO Works Under the Hood (Epoll / Kqueue Event Loop)</h3>
      <p style="color: var(--text-secondary); margin-bottom: 0.5rem;">
        In <code>asyncio</code>, execution is single-threaded cooperative multitasking:
      </p>
      <pre><code class="language-python">import asyncio

async def fetch_data():
    print("Start fetch...")
    await asyncio.sleep(1) # Yields execution back to event loop!
    print("Done fetch!")

async def main():
    # Runs both coroutines concurrently on a single OS thread!
    await asyncio.gather(fetch_data(), fetch_data())

asyncio.run(main())</code></pre>
      <p style="color: var(--text-secondary); margin-top: 0.5rem;">
        When <code>await</code> is called, the coroutine suspends its generator frame and yields control back to the <strong>Event Loop</strong>. The event loop registers the socket file descriptor with the OS kernel's <code>epoll</code> (Linux) or <code>kqueue</code> (macOS). When data arrives, the OS notifies the loop, which wakes up the suspended coroutine.
      </p>
    </section>

    <!-- SECTION 4: INTERVIEW TRAPS -->
    <section id="interview-traps" class="section-block">
      <div class="section-head">
        <h2 class="section-title">⚠️ High-Frequency Python Traps</h2>
        <span class="pill pill-rose">Recruiter Traps</span>
      </div>

      <div class="callout callout-trap">
        <div class="callout-title">Trap #1: Mutable Default Arguments Pitfall</div>
        <pre><code class="language-python">def append_to(element, target_list=[]):
    target_list.append(element)
    return target_list

print(append_to(1)) # Output: [1]
print(append_to(2)) # Output: [1, 2] -- TRAP! Not [2]!</code></pre>
        <p><strong>Why:</strong> Default function arguments are evaluated <strong>once at function definition time</strong> (when the module is loaded), NOT when the function is called! The empty list <code>[]</code> is shared across all subsequent invocations.</p>
        <p><strong>The Fix:</strong> Use <code>None</code> as the default sentinel value:</p>
        <pre><code class="language-python">def append_to(element, target_list=None):
    if target_list is None:
        target_list = []
    target_list.append(element)
    return target_list</code></pre>
      </div>

      <div class="callout callout-trap">
        <div class="callout-title">Trap #2: "is" vs "==" and Small Integer Caching</div>
        <pre><code class="language-python">a = 256; b = 256
print(a is b) # True!

x = 257; y = 257
print(x is b) # False! (In standard REPL)</code></pre>
        <p><strong>Why:</strong> <code>==</code> tests for equality of values. <code>is</code> tests for <strong>memory address identity</strong> (<code>id(a) == id(b)</code>). CPython pre-allocates and caches an internal array of all integers between <strong>-5 and 256</strong> at interpreter startup! Numbers in this range always share the same memory address, whereas numbers outside this range create distinct heap objects.</p>
      </div>
    </section>

    <!-- SECTION 5: FLASHCARDS (10 GFG QUESTIONS) -->
    <section id="flashcards" class="section-block">
      <div class="section-head">
        <h2 class="section-title">🎯 10 High-Frequency GFG Interview Q&As (Self-Assessment)</h2>
        <span class="pill pill-blue">10 Questions</span>
      </div>

      <details class="faq-accordion">
        <summary>Q1: Why does Python have a GIL and can you remove it?</summary>
        <div class="faq-body">
          CPython uses the <strong>GIL (Global Interpreter Lock)</strong> because its memory management relies on reference counting. Without the GIL, every single reference count increment and decrement would require fine-grained thread mutex locks, which would cripple single-threaded performance by 2x to 3x!<br>
          • <strong>Free-threaded Python (PEP 703):</strong> Python 3.13 introduces an experimental build option (<code>--disable-gil</code>) that replaces the GIL with mimalloc-based biased reference counting.
        </div>
      </details>

      <details class="faq-accordion">
        <summary>Q2: How does __slots__ save 40-50% memory in Python classes?</summary>
        <div class="faq-body">
          By default, every Python instance stores its attributes dynamically inside a dictionary (<code>self.__dict__</code>). A Python hash dictionary carries substantial memory overhead (hash table array, key pointers, capacity expansion).<br>
          When you define <code>__slots__ = ('name', 'age')</code>:
          <ul>
            <li>Python allocates a fixed-size C array of pointers instead of a dynamic dictionary.</li>
            <li>No <code>__dict__</code> is created for instances!</li>
            <li>Attribute lookups become direct array offset indexing, reducing per-object memory from ~150 bytes to ~48 bytes.</li>
          </ul>
        </div>
      </details>

      <details class="faq-accordion">
        <summary>Q3: What is the difference between copy.copy() (Shallow Copy) and copy.deepcopy()?</summary>
        <div class="faq-body">
          • <strong>Shallow Copy (<code>copy.copy()</code>):</strong> Constructs a new container object, but populates it with <em>references</em> to the objects found in the original. Modifying nested mutable objects (e.g. lists inside a list) mutates both copies!<br>
          • <strong>Deep Copy (<code>copy.deepcopy()</code>):</strong> Recursively clones the entire object hierarchy, copying all nested objects and circular references into brand new memory addresses.
        </div>
      </details>

      <details class="faq-accordion">
        <summary>Q4: How do Generators (yield) work and why are they memory efficient?</summary>
        <div class="faq-body">
          A regular function computes its entire result and returns it at once, allocating memory for all elements (e.g. a list of 10,000,000 integers takes ~800MB RAM).<br>
          A <strong>Generator function</strong> uses <code>yield</code>:
          <ul>
            <li>When <code>yield</code> is encountered, the function's execution state (local variables, instruction pointer) is frozen in a <code>PyFrameObject</code> and returned to the caller.</li>
            <li>Subsequent calls to <code>next()</code> resume execution from where it left off.</li>
            <li>Memory footprint is strictly <strong>$O(1)$ constant memory</strong> regardless of data size!</li>
          </ul>
        </div>
      </details>

      <details class="faq-accordion">
        <summary>Q5: What is the difference between *args and **kwargs?</summary>
        <div class="faq-body">
          • <code>*args</code> collects positional arguments passed beyond the formal parameter list into a <strong>tuple</strong>.<br>
          • <code>**kwargs</code> collects named keyword arguments passed beyond the formal parameter list into a <strong>dictionary</strong>.<br>
          Order in function definition: <code>def func(required, *args, default=val, **kwargs):</code>.
        </div>
      </details>

      <details class="faq-accordion">
        <summary>Q6: What does @functools.wraps do and why is it mandatory in decorators?</summary>
        <div class="faq-body">
          When a function is wrapped by a decorator, the decorated function takes on the name and docstring of the internal wrapper function (e.g. <code>my_func.__name__</code> becomes <code>"wrapper"</code>), breaking debugging, logging, and reflection tools.<br>
          Adding <code>@functools.wraps(func)</code> to the wrapper copies over the original function's metadata (<code>__name__</code>, <code>__doc__</code>, <code>__annotations__</code>).
        </div>
      </details>

      <details class="faq-accordion">
        <summary>Q7: How does Python's Garbage Collector detect Cyclic References?</summary>
        <div class="faq-body">
          Python uses an algorithm that tracks all container objects (lists, dicts, custom classes) in a doubly-linked list:
          <ol style="margin-left: 1.2rem;">
            <li>For each container object, it sets a trial reference count equal to <code>ob_refcnt</code>.</li>
            <li>It iterates through all objects and decrements the trial reference count for every reference pointing from one tracked container to another.</li>
            <li>Any object whose trial count drops to 0 has all its incoming references originating from within the isolated cycle itself!</li>
            <li>These unreachable circular clusters are broken and freed.</li>
          </ol>
        </div>
      </details>

      <details class="faq-accordion">
        <summary>Q8: What is Method Resolution Order (MRO) and the C3 Linearization Algorithm?</summary>
        <div class="faq-body">
          In multiple inheritance (e.g. Diamond Problem: Class D inherits from B and C, which both inherit from A), Python determines which method to execute using <strong>C3 Linearization (MRO)</strong>.<br>
          It guarantees two properties: (1) Children precede their parents, and (2) The order of base classes in the class declaration is preserved. You can inspect any class's resolution order via <code>ClassName.__mro__</code>.
        </div>
      </details>

      <details class="faq-accordion">
        <summary>Q9: What is the difference between List Comprehension and Generator Expression?</summary>
        <div class="faq-body">
          • <strong>List Comprehension:</strong> <code>[x*2 for x in range(1000)]</code>. Enclosed in brackets <code>[]</code>; evaluates eagerly and allocates full list in memory immediately.<br>
          • <strong>Generator Expression:</strong> <code>(x*2 for x in range(1000))</code>. Enclosed in parentheses <code>()</code>; evaluates lazily on-demand, consuming near zero memory.
        </div>
      </details>

      <details class="faq-accordion">
        <summary>Q10: How do you achieve true CPU parallelism in Python?</summary>
        <div class="faq-body">
          To bypass the GIL and utilize 100% of all CPU cores:
          <ul>
            <li><strong>multiprocessing:</strong> Use <code>concurrent.futures.ProcessPoolExecutor</code> or <code>multiprocessing.Pool</code> to spawn child processes across CPU cores.</li>
            <li><strong>C / Cython Extensions:</strong> Release the GIL in C extensions during compute loops using <code>Py_BEGIN_ALLOW_THREADS</code> (as done in NumPy, PyTorch, OpenCV).</li>
            <li><strong>Distributed Task Workers:</strong> Use Celery or Ray to distribute tasks across cluster nodes.</li>
          </ul>
        </div>
      </details>
    </section>
    """
    
    rendered_content = content.replace("__SVG_GIL_EXECUTION__", svg_gil).replace("__SVG_GENERATIONAL_GC__", svg_gc)
    return toc, rendered_content
