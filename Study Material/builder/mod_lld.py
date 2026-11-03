# mod_lld.py - Low-Level Design & Design Patterns Module Generator

def get_content():
    toc = [
        ("rapid-recall", "⚡ 10-Min Rapid Recall Sheet"),
        ("visual-diagrams", "📊 Visual UML Class Diagrams"),
        ("core-deep-dives", "🧠 SOLID, LRU Cache & Design Patterns"),
        ("interview-traps", "⚠️ High-Frequency LLD & OOD Traps"),
        ("flashcards", "🎯 10 High-Frequency GFG Interview Q&As")
    ]

    # SVG 1: LRU Cache UML Class Diagram
    svg_lru = """
    <svg viewBox="0 0 860 320" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="lld-arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8" />
        </marker>
        <marker id="comp-arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 5 L 5 0 L 10 5 L 5 10 z" fill="#c084fc" />
        </marker>
      </defs>

      <!-- Node Class -->
      <rect x="30" y="40" width="220" height="150" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="2" />
      <rect x="30" y="40" width="220" height="30" rx="6" fill="#0369a1" />
      <text x="140" y="60" fill="#ffffff" font-size="12" font-weight="800" text-anchor="middle">&laquo;struct&raquo; Node</text>
      <text x="45" y="90" fill="#f1f5f9" font-size="10">+ key: int</text>
      <text x="45" y="110" fill="#f1f5f9" font-size="10">+ value: int</text>
      <text x="45" y="130" fill="#38bdf8" font-size="10">+ prev: Node*</text>
      <text x="45" y="150" fill="#38bdf8" font-size="10">+ next: Node*</text>
      <line x1="30" y1="162" x2="250" y2="162" stroke="#334155" />
      <text x="45" y="178" fill="#94a3b8" font-size="9">+ Node(int k, int v)</text>

      <!-- DoublyLinkedList Class -->
      <rect x="310" y="40" width="240" height="210" rx="6" fill="#1e293b" stroke="#c084fc" stroke-width="2" />
      <rect x="310" y="40" width="240" height="30" rx="6" fill="#581c87" />
      <text x="430" y="60" fill="#ffffff" font-size="12" font-weight="800" text-anchor="middle">&laquo;class&raquo; DoublyLinkedList</text>
      <text x="325" y="90" fill="#f1f5f9" font-size="10">- head: Node* (dummy)</text>
      <text x="325" y="110" fill="#f1f5f9" font-size="10">- tail: Node* (dummy)</text>
      <line x1="310" y1="122" x2="550" y2="122" stroke="#334155" />
      <text x="325" y="140" fill="#34d399" font-size="10">+ addNodeToHead(Node*): void</text>
      <text x="325" y="160" fill="#34d399" font-size="10">+ removeNode(Node*): void</text>
      <text x="325" y="180" fill="#34d399" font-size="10">+ moveToHead(Node*): void</text>
      <text x="325" y="200" fill="#34d399" font-size="10">+ popTail(): Node*</text>
      <text x="325" y="225" fill="#bae6fd" font-size="9">All Operations: Strict O(1)!</text>

      <!-- LRUCache Class -->
      <rect x="610" y="40" width="230" height="230" rx="6" fill="#1e293b" stroke="#34d399" stroke-width="2" />
      <rect x="610" y="40" width="230" height="30" rx="6" fill="#065f46" />
      <text x="725" y="60" fill="#ffffff" font-size="12" font-weight="800" text-anchor="middle">&laquo;class&raquo; LRUCache</text>
      <text x="625" y="90" fill="#f1f5f9" font-size="10">- capacity: int</text>
      <text x="625" y="110" fill="#f1f5f9" font-size="10">- size: int</text>
      <text x="625" y="130" fill="#fbbf24" font-size="10">- map: unordered_map&lt;int, Node*&gt;</text>
      <text x="625" y="150" fill="#c084fc" font-size="10">- dll: DoublyLinkedList</text>
      <line x1="610" y1="162" x2="840" y2="162" stroke="#334155" />
      <text x="625" y="185" fill="#38bdf8" font-size="11" font-weight="700">+ get(key: int): int</text>
      <text x="625" y="210" fill="#38bdf8" font-size="11" font-weight="700">+ put(key: int, val: int): void</text>
      <text x="625" y="240" fill="#a7f3d0" font-size="9">HashMap provides O(1) Search</text>
      <text x="625" y="255" fill="#a7f3d0" font-size="9">DLL provides O(1) Eviction</text>

      <!-- Connecting Lines -->
      <line x1="250" y1="115" x2="300" y2="115" stroke="#38bdf8" stroke-width="1.5" marker-end="url(#lld-arrow)" />
      <line x1="550" y1="140" x2="600" y2="140" stroke="#c084fc" stroke-width="1.5" marker-end="url(#comp-arrow)" />

      <text x="430" y="295" fill="#38bdf8" font-size="13" font-weight="800" text-anchor="middle">UML Class Diagram: Low-Level Design (LLD) of an O(1) In-Memory LRU Cache</text>
    </svg>
    """

    content = r"""
    <!-- SECTION 1: RAPID RECALL -->
    <section id="rapid-recall" class="section-block">
      <div class="section-head">
        <h2 class="section-title">⚡ 10-Minute Rapid Recall Cheat Sheet</h2>
        <span class="pill pill-purple">OOD & Patterns</span>
      </div>

      <!-- SOLID Principles Table -->
      <h3 style="font-size: 1rem; color: var(--accent-purple); margin: 1rem 0 0.5rem;">1. SOLID Principles Master Matrix</h3>
      <div class="table-container">
        <table class="dense-table">
          <thead>
            <tr>
              <th>Principle</th>
              <th>Formal Rule</th>
              <th>Common Violation (Anti-Pattern)</th>
              <th>Refactored Solution</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>S - Single Responsibility</strong></td>
              <td>A class should have one, and only one, reason to change.</td>
              <td>A <code>User</code> class that manages user properties, writes to database, AND sends welcome emails.</td>
              <td>Separate into <code>User</code> (model), <code>UserRepository</code> (database), and <code>EmailService</code> (notifications).</td>
            </tr>
            <tr>
              <td><strong>O - Open / Closed</strong></td>
              <td>Software entities should be <strong>open for extension</strong>, but <strong>closed for modification</strong>.</td>
              <td>Using giant <code>if/else</code> or <code>switch</code> blocks to calculate discounts for each new customer type.</td>
              <td>Use the <strong>Strategy Pattern</strong> or Polymorphism with a common <code>DiscountStrategy</code> interface.</td>
            </tr>
            <tr>
              <td><strong>L - Liskov Substitution</strong></td>
              <td>Subtypes must be substitutable for their base types without altering program correctness.</td>
              <td><strong>Square inherits from Rectangle:</strong> setting <code>width</code> alters <code>height</code>, breaking client expectations!</td>
              <td>Do not inherit Square from Rectangle; have both implement a shared <code>Shape</code> interface with <code>getArea()</code>.</td>
            </tr>
            <tr>
              <td><strong>I - Interface Segregation</strong></td>
              <td>Clients should not be forced to depend upon interfaces they do not use (fat interfaces).</td>
              <td>A monolithic <code>Machine</code> interface with <code>print()</code>, <code>scan()</code>, and <code>fax()</code> forced onto a simple printer.</td>
              <td>Split into fine-grained interfaces: <code>Printer</code>, <code>Scanner</code>, and <code>FaxMachine</code>.</td>
            </tr>
            <tr>
              <td><strong>D - Dependency Inversion</strong></td>
              <td>High-level modules should not depend on low-level modules; both should depend on abstractions.</td>
              <td>A <code>PaymentProcessor</code> directly instantiating <code>new StripeClient()</code> inside its constructor.</td>
              <td>Inject a <code>PaymentGateway</code> interface into <code>PaymentProcessor</code> (Dependency Injection).</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- GoF Design Patterns Master Matrix -->
      <h3 style="font-size: 1rem; color: var(--accent-blue); margin: 1.5rem 0 0.5rem;">2. Top 10 High-Frequency Design Patterns Cheat Sheet</h3>
      <div class="table-container">
        <table class="dense-table">
          <thead>
            <tr>
              <th>Pattern</th>
              <th>Category</th>
              <th>Intent / Core Mechanism</th>
              <th>Real-World / Standard Library Example</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Singleton</strong></td>
              <td>Creational</td>
              <td>Ensures a class has only one instance and provides a global access point.</td>
              <td>Thread-safe Database Connection Pool, Logger, Hardware device driver.</td>
            </tr>
            <tr>
              <td><strong>Factory Method</strong></td>
              <td>Creational</td>
              <td>Defines an interface for creating objects, letting subclasses decide which class to instantiate.</td>
              <td><code>LoggerFactory.getLogger()</code>, Cross-platform GUI button creation.</td>
            </tr>
            <tr>
              <td><strong>Builder</strong></td>
              <td>Creational</td>
              <td>Constructs complex objects step-by-step, avoiding telescopic constructors with 10+ arguments.</td>
              <td><code>HttpRequest.newBuilder().uri(...).GET().build()</code>.</td>
            </tr>
            <tr>
              <td><strong>Adapter</strong></td>
              <td>Structural</td>
              <td>Converts the interface of a legacy or third-party class into another interface clients expect.</td>
              <td><code>Arrays.asList()</code>, wrapping a legacy XML payment API to conform to JSON interface.</td>
            </tr>
            <tr>
              <td><strong>Decorator</strong></td>
              <td>Structural</td>
              <td>Attaches additional responsibilities to an object dynamically without subclassing.</td>
              <td>Java I/O: <code>new BufferedReader(new FileReader("file.txt"))</code>; Python function decorators.</td>
            </tr>
            <tr>
              <td><strong>Proxy</strong></td>
              <td>Structural</td>
              <td>Provides a surrogate or placeholder for another object to control access, caching, or lazy loading.</td>
              <td>Hibernate Lazy Loading proxy, Virtual Proxy, Protection Proxy (auth checks).</td>
            </tr>
            <tr>
              <td><strong>Strategy</strong></td>
              <td>Behavioral</td>
              <td>Defines a family of interchangeable algorithms and makes them interchangeable at runtime.</td>
              <td><code>Collections.sort(list, Comparator)</code>, Payment strategies (CreditCard, PayPal, UPI).</td>
            </tr>
            <tr>
              <td><strong>Observer</strong></td>
              <td>Behavioral</td>
              <td>Defines a one-to-many dependency so that when one object changes state, all dependents are notified.</td>
              <td>GUI Event Listeners, Kafka Event Bus, Reactive Streams, Model-View-Controller (MVC).</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- SECTION 2: VISUAL DIAGRAMS -->
    <section id="visual-diagrams" class="section-block">
      <div class="section-head">
        <h2 class="section-title">📊 Visual UML Class Diagrams</h2>
        <span class="pill pill-emerald">LLD Architecture</span>
      </div>

      <div class="svg-diagram-card">
        __SVG_LRU_CACHE__
        <div class="diagram-caption">Figure 11.1: Complete UML Class Architecture for an O(1) LRU Cache: Hash Map + Doubly-Linked List with Sentinel Dummy Nodes.</div>
      </div>
    </section>

    <!-- SECTION 3: CORE DEEP DIVES -->
    <section id="core-deep-dives" class="section-block">
      <div class="section-head">
        <h2 class="section-title">🧠 SOLID, LRU Cache & Design Patterns</h2>
        <span class="pill pill-purple">Low-Level Code Implementations</span>
      </div>

      <!-- LRU Cache Implementation -->
      <h3 style="color: var(--accent-purple); font-size: 1.1rem; margin-top: 1rem;">1. Complete Production-Grade LRU Cache Implementation (C++)</h3>
      <p style="color: var(--text-secondary); margin-bottom: 0.5rem;">
        Combining <code>std::unordered_map</code> for $O(1)$ search and a <code>DoublyLinkedList</code> with dummy <code>head</code> and <code>tail</code> nodes to avoid edge-case null checks:
      </p>
      <pre><code class="language-cpp">#include &lt;unordered_map&gt;

class LRUCache {
    struct Node {
        int key, val;
        Node *prev = nullptr, *next = nullptr;
        Node(int k, int v) : key(k), val(v) {}
    };

    int capacity;
    std::unordered_map&lt;int, Node*&gt; cache;
    Node *head, *tail; // Dummy sentinel nodes

    void addNode(Node* node) {
        node->next = head->next;
        node->prev = head;
        head->next->prev = node;
        head->next = node;
    }

    void removeNode(Node* node) {
        Node* prevNode = node->prev;
        Node* nextNode = node->next;
        prevNode->next = nextNode;
        nextNode->prev = prevNode;
    }

    void moveToHead(Node* node) {
        removeNode(node);
        addNode(node);
    }

    Node* popTail() {
        Node* res = tail->prev;
        removeNode(res);
        return res;
    }

public:
    LRUCache(int cap) : capacity(cap) {
        head = new Node(-1, -1);
        tail = new Node(-1, -1);
        head->next = tail;
        tail->prev = head;
    }

    int get(int key) {
        if (cache.find(key) == cache.end()) return -1;
        Node* node = cache[key];
        moveToHead(node); // Mark as most recently used!
        return node->val;
    }

    void put(int key, int value) {
        if (cache.find(key) != cache.end()) {
            Node* node = cache[key];
            node->val = value;
            moveToHead(node);
        } else {
            Node* newNode = new Node(key, value);
            cache[key] = newNode;
            addNode(newNode);

            if (cache.size() > capacity) {
                Node* lru = popTail(); // Evict least recently used!
                cache.erase(lru->key);
                delete lru;
            }
        }
    }
};</code></pre>

      <!-- Thread-Safe Singleton -->
      <h3 style="color: var(--accent-emerald); font-size: 1.1rem; margin-top: 1.5rem;">2. Thread-Safe Singleton Pattern (Meyers' Singleton vs Double-Checked Locking)</h3>
      <p style="color: var(--text-secondary); margin-bottom: 0.5rem;">
        In modern C++11, <strong>Meyers' Singleton</strong> is guaranteed thread-safe by the C++ standard (§6.7) with zero explicit mutexes:
      </p>
      <pre><code class="language-cpp">class DatabaseConnection {
private:
    DatabaseConnection() { /* Connect to DB */ }
    ~DatabaseConnection() = default;

public:
    DatabaseConnection(const DatabaseConnection&) = delete;
    DatabaseConnection& operator=(const DatabaseConnection&) = delete;

    // Guaranteed thread-safe initialization by C++11 runtime!
    static DatabaseConnection& getInstance() {
        static DatabaseConnection instance; // Initialized exactly once!
        return instance;
    }
};</code></pre>
    </section>

    <!-- SECTION 4: INTERVIEW TRAPS -->
    <section id="interview-traps" class="section-block">
      <div class="section-head">
        <h2 class="section-title">⚠️ High-Frequency LLD & OOD Traps</h2>
        <span class="pill pill-rose">Interview Traps</span>
      </div>

      <div class="callout callout-trap">
        <div class="callout-title">Trap #1: Liskov Substitution Principle (Square vs Rectangle)</div>
        <p><strong>The Question:</strong> "Should a Square class inherit from a Rectangle class in OOP?"</p>
        <p><strong>The Trap Answer:</strong> "Yes, because mathematically all squares are rectangles." (Fails interview!)</p>
        <p><strong>The Engineering Reality:</strong> <em>No!</em> In OOP, behavior matters, not mathematical taxonomies. If <code>Square</code> inherits from <code>Rectangle</code>:</p>
        <pre><code class="language-cpp">void resize(Rectangle& r) {
    r.setWidth(5);
    r.setHeight(10);
    assert(r.getArea() == 50); // FAILS for Square! Setting height alters width to 10!
}</code></pre>
        <p>A client expecting a Rectangle will encounter broken invariants when passed a Square. This strictly violates the Liskov Substitution Principle (LSP).</p>
      </div>

      <div class="callout callout-trap">
        <div class="callout-title">Trap #2: Why Double-Checked Locking Failed in C++98 / Java 1.4</div>
        <p>In naive double-checked locking without modern memory barriers:</p>
        <pre><code class="language-cpp">if (instance == nullptr) {
    lock();
    if (instance == nullptr) {
        instance = new Singleton(); // HAZARD: Instruction reordering!
    }
}</code></pre>
        <p>The expression <code>instance = new Singleton()</code> involves 3 steps: (1) Allocate memory, (2) Construct object, (3) Assign pointer. Due to CPU out-of-order execution, the compiler may execute step 3 before step 2! Another thread checks <code>instance == nullptr</code>, sees a non-null pointer, and attempts to use the <em>unconstructed object</em>, causing crashes! In modern C++, solved via <code>std::atomic</code> with acquire-release memory order or Meyers' Singleton.</p>
      </div>
    </section>

    <!-- SECTION 5: FLASHCARDS (10 GFG QUESTIONS) -->
    <section id="flashcards" class="section-block">
      <div class="section-head">
        <h2 class="section-title">🎯 10 High-Frequency GFG Interview Q&As (Self-Assessment)</h2>
        <span class="pill pill-blue">10 Questions</span>
      </div>

      <details class="faq-accordion">
        <summary>Q1: What is the difference between Factory Method and Abstract Factory?</summary>
        <div class="faq-body">
          • <strong>Factory Method:</strong> Uses inheritance to create a single product. Subclasses override the factory method to return a specific subclass (e.g. <code>Dialog.createButton()</code> returns <code>WindowsButton</code> or <code>MacButton</code>).<br>
          • <strong>Abstract Factory:</strong> Uses composition to create a <strong>family of related or dependent products</strong> without specifying their concrete classes (e.g. <code>GUIFactory.createButton()</code> AND <code>GUIFactory.createCheckbox()</code> for Windows vs Mac).
        </div>
      </details>

      <details class="faq-accordion">
        <summary>Q2: What is the difference between Strategy Pattern and State Pattern?</summary>
        <div class="faq-body">
          While both share nearly identical UML class structures, their <strong>intent</strong> differs completely:
          <ul>
            <li><strong>Strategy Pattern:</strong> The client chooses a strategy algorithm upfront and passes it to the context. Strategies are independent and unaware of each other (e.g. Sorting via QuickSort vs MergeSort).</li>
            <li><strong>State Pattern:</strong> The context changes its behavior dynamically as its internal state changes. Concrete state classes hold references to the context and trigger state transitions (e.g. Vending Machine transitioning from <code>NoCoinState</code> &rarr; <code>HasCoinState</code> &rarr; <code>DispenseState</code>).</li>
          </ul>
        </div>
      </details>

      <details class="faq-accordion">
        <summary>Q3: How do you design a Parking Lot system (Key Classes & Methods)?</summary>
        <div class="faq-body">
          Core class hierarchy for Parking Lot LLD:
          <ol style="margin-left: 1.2rem;">
            <li><strong>Vehicle (Abstract):</strong> <code>licensePlate</code>, <code>VehicleType</code> (Motorcycle, Car, Truck).</li>
            <li><strong>ParkingSpot (Abstract):</strong> <code>spotNumber</code>, <code>SpotType</code>, <code>isAvailable</code>, <code>park(Vehicle)</code>, <code>vacate()</code>.</li>
            <li><strong>ParkingLevel:</strong> <code>levelNumber</code>, <code>List&lt;ParkingSpot&gt;</code>, <code>findAvailableSpot(VehicleType)</code>.</li>
            <li><strong>ParkingLot (Singleton):</strong> <code>List&lt;ParkingLevel&gt;</code>, <code>assignTicket(Vehicle)</code>, <code>processPayment(Ticket)</code>.</li>
            <li><strong>Ticket:</strong> <code>ticketId</code>, <code>entryTime</code>, <code>spotNumber</code>, <code>feeCalculationStrategy</code>.</li>
          </ol>
        </div>
      </details>

      <details class="faq-accordion">
        <summary>Q4: What is the difference between Adapter, Facade, and Decorator patterns?</summary>
        <div class="faq-body">
          • <strong>Adapter Pattern:</strong> Converts an interface into an expected interface (translates between two incompatible interfaces without changing behavior).<br>
          • <strong>Facade Pattern:</strong> Simplifies a complex subsystem by providing a single higher-level unified interface (e.g. <code>ComputerFacade.start()</code> calls CPU, RAM, and HardDrive).<br>
          • <strong>Decorator Pattern:</strong> Dynamically enhances an object with new behaviors without modifying its interface (wraps an object while implementing the exact same interface).
        </div>
      </details>

      <details class="faq-accordion">
        <summary>Q5: Why is "Favor Composition Over Inheritance" a fundamental OOP guideline?</summary>
        <div class="faq-body">
          Inheritance creates tight compile-time coupling (White-box reuse); any change in the base class can break subclasses. It also leads to combinatorial class explosion (e.g. <code>FastCar</code>, <code>SlowCar</code>, <code>ElectricFastCar</code>, <code>ElectricSlowCar</code>).<br>
          <strong>Composition (HAS-A):</strong> Decouples behavior into pluggable components at runtime (Black-box reuse). A <code>Car</code> simply holds an <code>Engine</code> interface and a <code>Transmission</code> interface, allowing components to be swapped dynamically!
        </div>
      </details>

      <details class="faq-accordion">
        <summary>Q6: What is the Command Pattern and how does it support Undo/Redo?</summary>
        <div class="faq-body">
          The <strong>Command Pattern</strong> encapsulates a request as an object, complete with all information needed to execute the action.<br>
          • The command interface defines <code>execute()</code> and <code>undo()</code>.<br>
          • An <code>Invoker</code> maintains an undo history stack: calling <code>execute()</code> pushes the command onto the history stack; clicking "Ctrl+Z" pops the command and calls its <code>undo()</code> method!
        </div>
      </details>

      <details class="faq-accordion">
        <summary>Q7: How do you design an Immutable Class in Java or C++?</summary>
        <div class="faq-body">
          An immutable class cannot be modified after construction:
          <ol style="margin-left: 1.2rem;">
            <li>Declare the class as <code>final</code> (prevents subclasses from overriding methods).</li>
            <li>Make all fields <code>private</code> and <code>final</code> (or <code>const</code> in C++).</li>
            <li>Do not provide any setter / mutating methods.</li>
            <li>If fields contain mutable objects (e.g. <code>Date</code>, <code>List</code>), return <strong>deep defensive copies</strong> in getters and constructor!</li>
          </ol>
        </div>
      </details>

      <details class="faq-accordion">
        <summary>Q8: What is the difference between Dependency Injection (DI) and Inversion of Control (IoC)?</summary>
        <div class="faq-body">
          • <strong>Inversion of Control (IoC):</strong> A general architectural design principle where the control of program flow is inverted from the application to a framework (e.g. Framework calls your code via lifecycle hooks).<br>
          • <strong>Dependency Injection (DI):</strong> A specific design pattern implementing IoC for object dependencies. Instead of a class creating its own dependencies (<code>new Database()</code>), dependencies are provided ("injected") from the outside via constructor, setter, or interface injection.
        </div>
      </details>

      <details class="faq-accordion">
        <summary>Q9: What is the Observer Pattern and how do you prevent Memory Leaks (The Lapsed Listener Problem)?</summary>
        <div class="faq-body">
          In the <strong>Observer Pattern</strong>, a Subject holds a list of Subscriber references.<br>
          <strong>The Lapsed Listener Problem:</strong> If an observer registers with a long-lived subject (e.g. global event bus), the subject retains a strong reference to the observer. Even if the observer is out of scope in the UI, the Garbage Collector cannot reclaim it, creating a severe memory leak!<br>
          <strong>Fix:</strong> Use <strong>Weak References</strong> (<code>std::weak_ptr</code> in C++ or <code>WeakReference</code> in Java) to hold observers in the subject's listener list.
        </div>
      </details>

      <details class="faq-accordion">
        <summary>Q10: What is the Template Method Pattern vs Strategy Pattern?</summary>
        <div class="faq-body">
          • <strong>Template Method:</strong> Uses inheritance. The base class defines the skeleton of an algorithm in a <code>final</code> method, deferring specific steps to abstract methods implemented by subclasses (Compile-time binding).<br>
          • <strong>Strategy:</strong> Uses composition. The context delegates the entire algorithm to a pluggable interface object (Runtime binding). Strategy is preferred when algorithms must be switched dynamically during program execution.
        </div>
      </details>
    </section>
    """
    
    rendered_content = content.replace("__SVG_LRU_CACHE__", svg_lru)
    return toc, rendered_content
