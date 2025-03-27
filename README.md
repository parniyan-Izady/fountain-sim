# FountainSync
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OS Fountain Simulator - Operating Systems Course Project</title>
</head>
<body>
    <h1>OS Fountain Simulator - Operating Systems Final Project</h1>
    <h2>Project Overview</h2>
    <p>
        This project is a Python-based multi-threaded simulation of urban fountains, developed as the final project for the Operating Systems course at Yazd University. The simulator demonstrates thread synchronization concepts through three distinct fountain activation patterns.
    </p>
    <h2>Features</h2>
    <h3>1. Activation Patterns</h3>
    <ul>
        <li><strong>Sequential Mode</strong>: Fountains activate one after another</li>
        <li><strong>Pairwise Mode</strong>: Fountains activate in synchronized pairs</li>
        <li><strong>Concurrent Mode</strong>: All fountains activate simultaneously with color variations</li>
    </ul>
    <h3>2. Dynamic Timing</h3>
    <p>Each fountain has random activation cycles (1-3) with random ON/OFF durations (1-5 seconds).</p>
    <h3>3. Color Variations</h3>
    <p>27 possible color combinations (Red, Green, Blue) for the concurrent activation mode.</p>
    <h3>4. Detailed Logging</h3>
    <p>Precise timestamped logging of all fountain activities and thread operations.</p>
    <h2>How to Run</h2>
    <ol>
        <li><strong>Prerequisites</strong>: Python 3.x with threading support</li>
        <li><strong>Running the Simulator</strong>:
            <pre><code>python fountain_simulation.py</code></pre>
        </li>
        <li><strong>Execution Flow</strong>:
            <p>The program automatically runs through all three activation modes sequentially, displaying detailed output in the console.</p>
        </li>
    </ol>
    <h2>Code Structure</h2>
    <ul>
        <li><code>Fountain</code> class: Thread subclass representing each fountain</li>
        <li><code>stage_1()</code>: Sequential activation implementation</li>
        <li><code>stage_2()</code>: Pairwise activation implementation</li>
        <li><code>stage_3()</code>: Concurrent activation with color variations</li>
        <li><code>main()</code>: Coordinates the execution flow</li>
    </ul>
    <h2>Technical Implementation</h2>
    <h3>Core Concepts Demonstrated</h3>
    <ul>
        <li>Thread creation and management using <code>threading</code></li>
        <li>Thread synchronization with <code>join()</code></li>
        <li>Randomized timing with <code>random</code> and <code>time</code></li>
        <li>Color combinations with <code>itertools.product</code></li>
    </ul>
    <h2>Challenges and Learnings</h2>
    <p><strong>Thread Coordination</strong>: Ensuring proper synchronization between fountain threads required careful implementation of join() operations.</p>
    <p><strong>Output Clarity</strong>: Managing console output from multiple simultaneous threads while maintaining readability was challenging.</p>
    <p><strong>Resource Management</strong>: Proper thread cleanup and resource release was crucial for stable execution.</p>
    <h2>Future Improvements</h2>
    <ul>
        <li><strong>Visualization</strong>: Adding a GUI using PyGame or tkinter</li>
        <li><strong>Configuration</strong>: Adding config files for fountain parameters</li>
        <li><strong>Advanced Patterns</strong>: Implementing more complex activation sequences</li>
    </ul>
    <h2>Conclusion</h2>
    <p>This project provided hands-on experience with core operating system concepts, particularly in thread management and synchronization. The fountain metaphor effectively demonstrates these concepts while creating an engaging simulation.</p>
    <h2>University Credit</h2>
    <p>Developed as part of the Operating Systems course curriculum at <a href="https://www.yazd.ac.ir" target="_blank">Yazd University</a>.</p>
</body>
</html>
