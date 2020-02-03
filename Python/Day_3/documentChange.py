PREFIX = '<span class="nb">'
POSTFIX = "</span>"
PRINT = "print"

doc_text = """<div class="section" id="first-steps-towards-programming">
<span id="tut-firststeps"></span><h2>3.2. First Steps Towards Programming<a class="headerlink" href="#first-steps-towards-programming" title="Permalink to this headline">¶</a></h2>
<p>Of course, we can use Python for more complicated tasks than adding two and two
together.  For instance, we can write an initial sub-sequence of the <em>Fibonacci</em>
series as follows:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="c1"># Fibonacci series:</span>
<span class="gp">... </span><span class="c1"># the sum of two elements defines the next</span>
<span class="gp">... </span><span class="n">a</span><span class="p">,</span> <span class="n">b</span> <span class="o">=</span> <span class="nb">0</span><span class="p">,</span> <span class="nb">1</span>
<span class="gp">&gt;&gt;&gt; </span><span class="k">while</span> <span class="n">b</span> <span class="o">&lt;</span> <span class="nb">10</span><span class="p">:</span>
<span class="gp">... </span>    <span class="nb">print</span> <span class="n">b</span>
<span class="gp">... </span>    <span class="n">a</span><span class="p">,</span> <span class="n">b</span> <span class="o">=</span> <span class="n">b</span><span class="p">,</span> <span class="n">a</span><span class="o">+</span><span class="n">b</span>
<span class="gp">...</span>
<span class="go">1</span>
<span class="go">1</span>
<span class="go">2</span>
<span class="go">3</span>
<span class="go">5</span>
<span class="go">8</span>
</pre></div>
</div>"""

PREFIX = '<span class="nb">'
POSTFIX = "</span>"
PRINT = "print"


def linefunc(line):
    [word, rest] = line.split(POSTFIX, 1)
    rest = rest[1:]
    updated_line = word + POSTFIX + "({})".format(rest)
    return updated_line


def blockfunc(blocks):
    updated_blocks = []
    for block in blocks:
        if block[:len(PRINT)] == PRINT:
            [line, rest] = block.split("\n", 1)
            updated_line = linefunc(line)
            updated_block = updated_line + "\n" + rest
            updated_blocks.append(updated_block)
        else:
            updated_blocks.append(block)
    return updated_blocks


def mainfunc():
    parts = doc_text.split(PREFIX)
    updated_blocks = blockfunc(parts)
    updated_doc = PREFIX.join(updated_blocks)
    print(updated_doc)


mainfunc()
