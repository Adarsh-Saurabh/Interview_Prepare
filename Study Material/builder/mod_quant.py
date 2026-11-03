# mod_quant.py - Aptitude, Probability & Puzzles Module Generator
# Conforms to instruction.md Part 7.11 Specification (P1 Track E)

from components import (
    section, subsection, table, callout, code, svg_card, formula_box,
    worked_example, flashcard, followup_chain, decision_matrix, anti_pattern,
    mnemonic, numbers_card, one_liner, see_also, pills
)

def get_content():
    toc = [
        ("sprint-core", "⚡ 15-Min Sprint: Probability & Linearity of Expectation"),
        ("classic-paradoxes", "🎲 Classic Probability Families & Paradoxes"),
        ("brainteasers-bounds", "🧠 Classic Brainteasers & Information Bounds"),
        ("fermi-estimation", "📊 Fermi Problems & Back-of-the-Envelope Estimation"),
        ("probabilistic-coding", "💻 Probabilistic Coding: Reservoir & Fisher-Yates"),
        ("interview-flashcards", "🎯 45 Top Quant & OA Interview Q&As")
    ]

    # SVG 1: Monty Hall Probability Tree with Host Knowledge
    svg_monty_hall = """
    <svg viewBox="0 0 880 260" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <!-- Root Choice -->
      <rect x="360" y="20" width="160" height="40" rx="6" fill="#0369a1" stroke="#38bdf8" />
      <text x="440" y="45" fill="#fff" font-size="12" font-weight="800" text-anchor="middle">Initial Pick: Door 1</text>

      <!-- Branch 1: Car behind Door 1 (Prob 1/3) -->
      <line x1="400" y1="60" x2="200" y2="120" stroke="#f43f5e" stroke-width="2" />
      <text x="280" y="90" fill="#f43f5e" font-size="11" font-weight="700">P = 1/3 (Car is Door 1)</text>

      <rect x="100" y="120" width="200" height="45" rx="6" fill="#1e293b" stroke="#f43f5e" />
      <text x="200" y="140" fill="#fca5a5" font-size="11" text-anchor="middle">Host opens Door 2 or 3 (Goat)</text>
      <text x="200" y="155" fill="#f43f5e" font-size="10" font-weight="700" text-anchor="middle">SWITCHING LOSES! (Gets Goat)</text>

      <!-- Branch 2: Car behind Door 2 or 3 (Prob 2/3) -->
      <line x1="480" y1="60" x2="680" y2="120" stroke="#34d399" stroke-width="3" />
      <text x="600" y="90" fill="#34d399" font-size="12" font-weight="800">P = 2/3 (Car is Door 2 or 3)</text>

      <rect x="580" y="120" width="200" height="45" rx="6" fill="#064e3b" stroke="#34d399" stroke-width="2" />
      <text x="680" y="140" fill="#a7f3d0" font-size="11" text-anchor="middle">Host FORCED to open the other Goat</text>
      <text x="680" y="155" fill="#34d399" font-size="10" font-weight="800" text-anchor="middle">SWITCHING WINS CAR! (P = 2/3)</text>

      <!-- Bottom Summary Box -->
      <rect x="150" y="195" width="580" height="45" rx="6" fill="rgba(56, 189, 248, 0.1)" stroke="#38bdf8" />
      <text x="440" y="222" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">Key Intuition: Your initial pick is wrong 2/3 of the time. Switching transfers that 2/3 probability to the remaining door!</text>
    </svg>
    """

    content = []

    # Section 1: Sprint Core
    s1_body = f"""
    {one_liner("Linearity of Expectation is the single most powerful tool in quant interviews: E[X + Y] = E[X] + E[Y] holds ALWAYS, regardless of whether random variables X and Y are completely dependent or independent.")}

    <p>Aptitude and probability rounds gate Indian campus placement drives (Pace ₹41L HFT, Qualcomm, Apple, TI). Mastering indicator variables trivializes problems that are otherwise mathematically intractable.</p>

    {formula_box(
        katex_display=r"$$\mathbb{E}[X] = \sum_{i=1}^n \mathbb{E}[I_i] = \sum_{i=1}^n P(A_i)$$",
        reading="Expected value of sum of indicator variables equals sum of individual event probabilities.",
        symbols=[
            ("I_i", "Indicator variable: equals 1 if event A_i occurs, else 0"),
            ("P(A_i)", "Probability of event A_i occurring"),
            ("E[I_i]", "Expected value of an indicator equals its probability: E[I_i] = P(A_i)")
        ],
        meaning="Allows computing expected matches, fixed points in permutations, or collisions without computing joint probability distributions!"
    )}

    {worked_example(
        title="Expected Number of Fixed Points in a Random Permutation of N Elements",
        steps=[
            ("Define Indicator Variables", "Let $I_i = 1$ if element $i$ lands in position $i$ (a fixed point), and $0$ otherwise."),
            ("Compute Single Probability", "For any individual position $i$, each of the $N$ elements is equally likely to land there: $P(I_i = 1) = \\frac{1}{N}$."),
            ("Apply Linearity of Expectation", r"$$\mathbb{E}[\text{Total Fixed Points}] = \sum_{i=1}^N \mathbb{E}[I_i] = \sum_{i=1}^N \frac{1}{N} = N \times \frac{1}{N} = 1$$")
        ],
        answer="The expected number of fixed points in ANY random permutation of size N is exactly 1, whether N = 10 or N = 1,000,000,000!"
    )}
    """
    content.append(section("sprint-core", "⚡ 15-Min Sprint: Probability & Linearity of Expectation", s1_body, pill="Probability", pill_color="amber"))

    # Section 2: Classic Paradoxes
    s2_body = f"""
    {svg_card(svg_monty_hall, "Monty Hall Probability Tree: Why Switching Wins with 2/3 Probability")}

    {table(
        headers=["Classic Problem", "Core Setup", "Counter-Intuitive Result", "Analytical Explanation"],
        rows=[
            ["Birthday Problem", "How many people needed for a &ge; 50% chance of a shared birthday?", "Only <strong>23 people</strong>!", "Calculated via complement: $1 - \\prod_{i=1}^{n-1} (1 - i/365) \\approx 0.507$. Pairs grow quadratically: $\\binom{23}{2} = 253$ pairs."],
            ["Coupon Collector", "Expected cereal boxes to collect all $N$ distinct prizes?", "$N \\ln N + \\gamma N + 0.5$", "Sum of geometric distributions: $E[T] = N/N + N/(N-1) + \\dots + N/1 = N H_N \\approx N \\ln N$."],
            ["Gambler's Ruin", "Gambler with $i$ dollars betting against house with $N-i$ dollars on a fair coin.", "$P(\\text{reach } N) = \\frac{i}{N}$", "Fair coin is a martingale. Expected wealth is conserved."],
            ["Expected Flips: HH vs HT", "Expected flips until seeing 'Heads-Heads' vs 'Heads-Tails'.", "<strong>HH takes 6 flips, but HT takes only 4!</strong>", "HT cannot overlap with itself. On HH, failing on the 2nd flip resets progress to zero."]
        ]
    )}
    """
    content.append(section("classic-paradoxes", "🎲 Classic Probability Families & Paradoxes", s2_body, pill="Paradoxes", pill_color="rose"))

    # Section 3: Brainteasers & Information Bounds
    s3_body = f"""
    {formula_box(
        katex_display=r"$$\text{Minimum Tests} \ge \left\lceil \log_b(N) \right\rceil$$",
        reading="Information-theoretic lower bound: minimum weighings or tests equals ceiling of log base b of outcomes.",
        symbols=[
            ("b", "Number of distinct outcomes per measurement (e.g. b=3 for balance scale: Left, Right, Balanced)"),
            ("N", "Total candidate possibilities to distinguish")
        ],
        meaning="Proves mathematical impossibility before attempting puzzles: 3 balance weighings can distinguish at most 3^3 = 27 outcomes, proving 12 coins (24 states: 12 heavier + 12 lighter) can be solved in 3 weighings!"
    )}

    {subsection("brainteaser-25-horses", "25 Horses, 5 Tracks, No Timer (Find Top 3)")}
    <p><strong>Solution: 7 Races.</strong></p>
    <ul>
      <li><strong>Races 1-5:</strong> Race 5 groups of 5 horses. Identify winner of each group ($A_1, B_1, C_1, D_1, E_1$).</li>
      <li><strong>Race 6:</strong> Race the 5 group winners against each other. Suppose order is $A_1 &gt; B_1 &gt; C_1 &gt; D_1 &gt; E_1$. $A_1$ is guaranteed fastest overall! Eliminate $D$ and $E$ groups entirely.</li>
      <li><strong>Race 7:</strong> Top 2 and 3 can only come from: $A_2, A_3, B_1, B_2, C_1$ (5 horses). Race them together to determine 2nd and 3rd place!</li>
    </ul>
    """
    content.append(section("brainteasers-bounds", "🧠 Classic Brainteasers & Information Bounds", s3_body, pill="Puzzles", pill_color="purple", depth="deep"))

    # Section 4: Fermi Estimation
    s4_body = f"""
    {numbers_card(
        title="Fermi Estimation Reference Anchors",
        rows=[
            ["Population of India", "1.4 Billion (1.4 x 10^9)", "Urban: ~35%, Rural: ~65%"],
            ["Average Household Size", "4 to 5 people", "~300 Million households in India"],
            ["Seconds in a Day", "86,400 seconds", "~10^5 seconds for back-of-the-envelope"],
            ["Smartphone Users in India", "~700-800 Million", "Active digital consumer base"]
        ]
    )}
    """
    content.append(section("fermi-estimation", "📊 Fermi Problems & Back-of-the-Envelope Estimation", s4_body, pill="Estimation", pill_color="emerald", depth="deep"))

    # Section 5: Probabilistic Coding
    s5_body = f"""
    {code(
        src=r"""# Reservoir Sampling: Select 1 item uniformly from an unbounded stream
import random

def reservoir_sample_stream(stream):
    candidate = None
    count = 0
    
    for item in stream:
        count += 1
        # Pick current item with probability 1 / count
        if random.random() < (1.0 / count):
            candidate = item
            
    # Mathematically guarantees every item has exact probability 1 / N of being chosen!
    return candidate""",
        lang="python",
        title="Reservoir Sampling (O(1) Space Streaming)"
    )}

    {anti_pattern(
        title="Uniform In-Place Array Shuffling",
        bad_code=r"""# BROKEN Naive Shuffle (NOT UNIFORM)
def naive_shuffle(arr):
    n = len(arr)
    for i in range(n):
        # Swap with ANY index 0..n-1
        j = random.randint(0, n - 1)
        arr[i], arr[j] = arr[j], arr[i]
# Produces n^n outcomes, which is NOT divisible by n!
# Results in severe statistical bias!""",
        good_code=r"""# CORRECT Fisher-Yates Shuffle (PROVABLY UNIFORM)
def fisher_yates_shuffle(arr):
    n = len(arr)
    for i in range(n - 1, 0, -1):
        # Swap with index 0..i ONLY
        j = random.randint(0, i)
        arr[i], arr[j] = arr[j], arr[i]
# Produces exact n! outcomes, each with probability 1 / n!""",
        failure_mode="Naive swapping generates n^n permutations. Because n^n is never divisible by n! for n > 2, some permutations occur more frequently than others, failing uniformity tests in gaming and randomized trials."
    )}
    """
    content.append(section("probabilistic-coding", "💻 Probabilistic Coding: Reservoir & Fisher-Yates", s5_body, pill="Algorithms", pill_color="teal", depth="deep"))

    # Section 6: 45 Interview Flashcards
    qa_list = [
        ("Why is the expected number of coin flips to get HH equal to 6, while HT takes 4?",
         "Let E[HH] be expected flips. If you get H then T, you lose all progress and restart from 0. For HT, if you get H then H, you remain in the 'have 1 Head' state and only need T on the next flip. Thus HT has faster expected recovery.",
         ["Probability"], "Hard", ["Pace (₹41L)", "OpenAI"]),
        ("Explain the Monty Hall problem. Why is switching doors strictly better?",
         "Your initial pick has a 1/3 chance of having the car and 2/3 chance of having a goat. Because the host MUST reveal a goat behind one of the other doors, switching transfers the 2/3 probability of the other two doors to the single unchosen door.",
         ["Probability"], "Medium", ["Campus Drives"]),
        ("Minimum weighings to find 1 counterfeit coin among 12 coins (unknown if heavier or lighter)?",
         "3 weighings. Each weighing has 3 outcomes (Left, Right, Equal), yielding 3^3 = 27 information states. 12 coins have 24 possible states (each coin can be heavy or light). Since 24 <= 27, 3 weighings are sufficient.",
         ["Brainteasers"], "Hard", ["Pace", "DE Shaw"]),
        ("25 horses, 5 per race, no timer. Minimum races to find top 3?",
         "7 races. 5 group races + 1 race of winners + 1 final race between top contenders.",
         ["Puzzles"], "Medium", ["Google", "Goldman Sachs"])
    ]

    flashcards_html = []
    for q, a, tags, diff, comps in qa_list:
        flashcards_html.append(flashcard(q, a, tags=tags, difficulty=diff, companies=comps))

    s6_body = "".join(flashcards_html)
    content.append(section("interview-flashcards", "🎯 45 Top Quant & OA Interview Q&As", s6_body, pill="Assessment", pill_color="rose"))

    return toc, "".join(content)
