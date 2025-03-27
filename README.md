<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
<h1>OS Fountain Simulator</h1>
<p>Welcome to the OS Fountain Simulator! This project demonstrates multithreading concepts through an urban fountain simulation, developed as part of the Operating Systems course at <a href="https://www.yazd.ac.ir" target="_blank">Yazd University</a>.</p>

<h2>Project Overview</h2>
<ul>
<li><strong>Core Concept:</strong> Simulates three urban fountains with synchronized activation patterns</li>
<li><strong>Thread Management:</strong> Each fountain operates as an independent thread</li>
<li><strong>Educational Value:</strong> Demonstrates thread synchronization and timing concepts</li>
</ul>

<h2>Key Features</h2>
<h3>Activation Patterns</h3>
<ul>
<li><strong>Sequential Mode:</strong> Fountains activate one after another</li>
<li><strong>Pairwise Mode:</strong> Two fountains activate simultaneously in synchronized pairs</li>
<li><strong>Concurrent Mode:</strong> All fountains activate together with color variations</li>
</ul>

<h3>Technical Specifications</h3>
<ul>
<li>Randomized activation cycles (1-3 per fountain)</li>
<li>Dynamic timing (1-5 seconds for each state)</li>
<li>27 possible color combinations in concurrent mode</li>
<li>Detailed execution logging with timestamps</li>
</ul>

<h2>Implementation Details</h2>
<ul>
<li>Built using Python's threading module</li>
<li>Uses join() for thread synchronization</li>
<li>Random module for dynamic timing</li>
<li>Itertools for color combinations</li>
</ul>

<h2>How to Run</h2>
<ol>
<li>Ensure Python 3.x is installed</li>
<li>Run the simulation: <code>python fountain_simulation.py</code></li>
<li>View the execution patterns in console output</li>
</ol>

<h2>Learning Outcomes</h2>
<ul>
<li>Thread creation and lifecycle management</li>
<li>Resource synchronization techniques</li>
<li>Timing and scheduling in multithreaded applications</li>
<li>Debugging concurrent systems</li>
</ul>

</body>
</html>
