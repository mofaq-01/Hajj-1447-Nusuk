with open('/home/ubuntu/report_project/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The employee chart should go AFTER the case assignment section block
# and BEFORE the SECTION 3 comment
# The exact marker is the closing </div> of the case assignment section + the SECTION 3 comment

old_marker = '''        </div>
    </div>

    <!-- ================================================
         SECTION 3: \u0625\u062d\u0635\u0627\u0626\u064a\u0627\u062a \u0627\u0644\u0631\u062d\u0644\u0627\u062a'''

new_marker = '''        </div>
    </div>

    <!-- ============================================================
         VISUALIZATION: Employee Trip Distribution Chart (Issue 3)
         ============================================================ -->
    <div class="section-block viz-section" id="empChartSection">
        <div class="section-hdr">
            <span>&#9632;</span> \u062a\u062d\u0644\u064a\u0644 \u0628\u064a\u0627\u0646\u0627\u062a \u062a\u0648\u0632\u064a\u0639 \u0627\u0644\u0631\u062d\u0644\u0627\u062a
        </div>
        <div class="section-body" style="padding: 14px;">
            <div style="position:relative; min-height:200px;">
                <canvas id="empDistChart" style="display:none; width:100%;"></canvas>
                <p id="empChartEmpty" style="text-align:center;color:#aaa;font-size:11px;font-family:'Cairo',sans-serif;padding:20px 0;">
                    \u0633\u064a\u062a\u0645 \u0639\u0631\u0636 \u0627\u0644\u0631\u0633\u0645 \u0627\u0644\u0628\u064a\u0627\u0646\u064a \u062a\u0644\u0642\u0627\u0626\u064a\u0627\u064b \u0639\u0646\u062f \u0625\u062f\u062e\u0627\u0644 \u0628\u064a\u0627\u0646\u0627\u062a \u0627\u0644\u0631\u062d\u0644\u0627\u062a
                </p>
            </div>
        </div>
    </div>

    <!-- ================================================
         SECTION 3: \u0625\u062d\u0635\u0627\u0626\u064a\u0627\u062a \u0627\u0644\u0631\u062d\u0644\u0627\u062a'''

if old_marker in content:
    content = content.replace(old_marker, new_marker, 1)
    print("Employee chart section inserted successfully!")
else:
    print("ERROR: Marker not found!")
    # Try to find what's actually there
    idx = content.find('SECTION 3')
    print("SECTION 3 context:")
    print(repr(content[idx-400:idx+50]))

with open('/home/ubuntu/report_project/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("File saved. empDistChart present:", "empDistChart" in content)
