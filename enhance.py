#!/usr/bin/env python3
"""
Apply all 5 approved enhancements to SourceB_Enhanced HTML report.
"""
import re

with open('/home/ubuntu/report_project/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ============================================================
# ISSUE 1: Fix @media print CSS page-break rules
# ============================================================

# Replace the print media block section that handles section-block and related
old_print_section_blocks = """    /* Keep section blocks together — avoid page breaks inside */
    .section-block { break-inside: avoid; }
    .bottom-grid   { break-inside: avoid; }
    .delivery-rate-box { break-inside: avoid; }"""

new_print_section_blocks = """    /* Allow natural page flow — sections break BETWEEN, not inside */
    .section-block {
        break-inside: avoid;
        page-break-inside: avoid;
        break-after: auto;
        page-break-after: auto;
    }
    .bottom-grid   { break-inside: avoid; page-break-inside: avoid; }
    .delivery-rate-box { break-inside: avoid; page-break-inside: avoid; }

    /* Large tables: allow page breaks between rows but keep thead with first row */
    .journey-tbl, .case-tbl, .sub-tbl, .attend-tbl {
        break-inside: auto;
        page-break-inside: auto;
    }
    .journey-tbl thead, .case-tbl thead, .sub-tbl thead, .attend-tbl thead {
        break-inside: avoid;
        page-break-inside: avoid;
        display: table-header-group;
    }
    .journey-tbl tbody tr, .case-tbl tbody tr, .sub-tbl tbody tr, .attend-tbl tbody tr {
        break-inside: avoid;
        page-break-inside: avoid;
    }

    /* Section headers: never orphaned at bottom of page */
    .section-hdr {
        break-after: avoid;
        page-break-after: avoid;
    }

    /* Visualization charts: avoid breaking inside */
    .viz-section {
        break-inside: avoid;
        page-break-inside: avoid;
    }"""

content = content.replace(old_print_section_blocks, new_print_section_blocks)

# Fix the report-page min-height in print
old_report_page_print = """    /* Report page: full width, no shadow, compact padding */
    .report-page {
        margin: 0;
        padding: 6mm 8mm;
        width: 100%;
        box-shadow: none;
        min-height: auto;
    }"""

new_report_page_print = """    /* Report page: full width, no shadow, compact padding — NO min-height so content flows freely */
    .report-page {
        margin: 0;
        padding: 6mm 8mm;
        width: 100%;
        box-shadow: none;
        min-height: 0 !important;
        height: auto !important;
        overflow: visible !important;
    }"""

content = content.replace(old_report_page_print, new_report_page_print)

print("Issue 1 (print CSS) applied:", old_print_section_blocks[:50] in content or new_print_section_blocks[:50] in content)

# ============================================================
# ISSUE 2: Fix green underlines alignment in balance tables
# ============================================================

# Fix nat-tag padding (reduce from 6px 12px to 2px 6px)
old_nat_tag = """.nat-tag {
    display: inline-block;
    background: var(--primary);
    color: white;
    border-radius: 6px;
    padding: 6px 12px;
    font-size: calc(var(--body-size) - 1px);
    font-family: 'Cairo', sans-serif;
    white-space: nowrap;
    margin: 4px 4px 4px 0;
    font-weight: 600;
    box-shadow: 0 2px 6px rgba(45, 125, 111, 0.2);
}"""

new_nat_tag = """.nat-tag {
    display: inline-block;
    background: var(--primary);
    color: white;
    border-radius: 6px;
    padding: 2px 6px;
    font-size: calc(var(--body-size) - 1px);
    font-family: 'Cairo', sans-serif;
    white-space: nowrap;
    margin: 2px 2px 2px 0;
    font-weight: 600;
    box-shadow: 0 1px 4px rgba(45, 125, 111, 0.2);
}"""

content = content.replace(old_nat_tag, new_nat_tag)

# Fix nat-tags-wrap min-height and padding
old_nat_tags_wrap = """.nat-tags-wrap {
    display: block;
    min-height: 26px;
    padding: 4px 6px;
    border: none;
    border-bottom: 1.5px solid rgba(45, 125, 111, 0.35);
    border-radius: 0;
    background: transparent;
    cursor: pointer;
    transition: border-color 0.2s, background-color 0.2s;
    text-align: right;
    direction: rtl;
    font-family: 'Cairo', sans-serif;
    font-size: calc(var(--body-size) - 1px);
}"""

new_nat_tags_wrap = """.nat-tags-wrap {
    display: block;
    min-height: 24px;
    padding: 3px 4px;
    border: none;
    border-bottom: 1.5px solid rgba(45, 125, 111, 0.35);
    border-radius: 0;
    background: transparent;
    cursor: pointer;
    transition: border-color 0.2s, background-color 0.2s;
    text-align: right;
    direction: rtl;
    font-family: 'Cairo', sans-serif;
    font-size: calc(var(--body-size) - 1px);
    box-sizing: border-box;
    line-height: 1.4;
    overflow: hidden;
}"""

content = content.replace(old_nat_tags_wrap, new_nat_tags_wrap)

# Fix searchable-field to be consistent
old_searchable = """.searchable-field {
    width: 100%;
    padding: 4px 6px;
    border: none;
    border-bottom: 1.5px solid rgba(45, 125, 111, 0.35);
    border-radius: 0;
    background: transparent;
    font-family: 'Cairo', sans-serif;
    font-size: calc(var(--body-size) - 1px);
    color: #444;
    cursor: pointer;
    text-align: right;
    min-height: 26px;
    line-height: 1.4;
    display: block;
    position: relative;
    transition: border-color 0.2s, background-color 0.2s;
    word-break: break-word;
    white-space: normal;
}"""

new_searchable = """.searchable-field {
    width: 100%;
    padding: 3px 4px;
    border: none;
    border-bottom: 1.5px solid rgba(45, 125, 111, 0.35);
    border-radius: 0;
    background: transparent;
    font-family: 'Cairo', sans-serif;
    font-size: calc(var(--body-size) - 1px);
    color: #444;
    cursor: pointer;
    text-align: right;
    min-height: 24px;
    line-height: 1.4;
    display: block;
    position: relative;
    transition: border-color 0.2s, background-color 0.2s;
    word-break: break-word;
    white-space: normal;
    box-sizing: border-box;
    overflow: hidden;
}"""

content = content.replace(old_searchable, new_searchable)

# Fix case-tbl td vertical-align to middle and add overflow hidden
old_case_tbl_td = """.case-tbl td {
    padding: 4px 6px;
    border-bottom: 1px solid var(--border);
    text-align: center;
    word-break: break-word;
    overflow-wrap: break-word;
    white-space: normal;
    vertical-align: middle;
}"""

new_case_tbl_td = """.case-tbl td {
    padding: 4px 6px;
    border-bottom: 1px solid var(--border);
    text-align: center;
    word-break: break-word;
    overflow-wrap: break-word;
    white-space: normal;
    vertical-align: middle;
    overflow: hidden;
}"""

content = content.replace(old_case_tbl_td, new_case_tbl_td)

# Fix sub-tbl td to have vertical-align middle
old_sub_tbl_td = """.sub-tbl td {
    padding: 4px 6px;
    border-bottom: 1px solid var(--border);
    text-align: center;
    word-break: break-word;
    overflow-wrap: break-word;
    white-space: normal;
}"""

new_sub_tbl_td = """.sub-tbl td {
    padding: 4px 6px;
    border-bottom: 1px solid var(--border);
    text-align: center;
    word-break: break-word;
    overflow-wrap: break-word;
    white-space: normal;
    vertical-align: middle;
    overflow: hidden;
}"""

content = content.replace(old_sub_tbl_td, new_sub_tbl_td)

# Fix number inputs in case-tbl to have consistent sizing
old_case_number = """.ftbl .vc input[type="number"],
.sub-tbl td input[type="number"] {
    border: none !important;
    border-bottom: 1.5px solid rgba(45, 125, 111, 0.35) !important;
    background: transparent !important;
    box-shadow: none !important;
    outline: none !important;
    padding: 2px 0 !important;
    border-radius: 0 !important;
    font-weight: 400;
    color: var(--dark);
    -moz-appearance: textfield;
    appearance: textfield;
}"""

new_case_number = """.ftbl .vc input[type="number"],
.sub-tbl td input[type="number"],
.case-tbl td input[type="number"] {
    border: none !important;
    border-bottom: 1.5px solid rgba(45, 125, 111, 0.35) !important;
    background: transparent !important;
    box-shadow: none !important;
    outline: none !important;
    padding: 3px 4px !important;
    border-radius: 0 !important;
    font-weight: 400;
    color: var(--dark);
    -moz-appearance: textfield;
    appearance: textfield;
    width: 100% !important;
    box-sizing: border-box !important;
    min-height: 24px;
    line-height: 1.4;
    display: block;
}"""

content = content.replace(old_case_number, new_case_number)

print("Issue 2 (underline alignment) applied")

# ============================================================
# ISSUE 3: Add horizontal bar chart after employee summary table
# ============================================================

# Find the employee summary section and add chart after it
# The summary section ends with </div> after empSummaryBody table
# We need to find the closing of the emp summary section block

emp_summary_section_end = """    </div><!-- end .report-page -->"""

emp_chart_html = """
    <!-- ============================================================
         VISUALIZATION: Employee Trip Distribution Chart (Issue 3)
         ============================================================ -->
    <div class="section-block viz-section" id="empChartSection">
        <div class="section-hdr">
            <span>&#9632;</span> تحليل بيانات توزيع الرحلات
        </div>
        <div class="section-body" style="padding: 14px;">
            <canvas id="empDistChart" style="max-height: 320px; width: 100%;"></canvas>
            <p id="empChartEmpty" style="text-align:center;color:#aaa;font-size:11px;font-family:'Cairo',sans-serif;padding:20px 0;">
                سيتم عرض الرسم البياني تلقائياً عند إدخال بيانات الرحلات
            </p>
        </div>
    </div>

    </div><!-- end .report-page -->"""

content = content.replace(emp_summary_section_end, emp_chart_html)

print("Issue 3 (emp chart placeholder) applied:", "empDistChart" in content)

# ============================================================
# ISSUE 4: Add donut chart + KPI cards after trip stats table
# ============================================================

# Find the delivery rate box and add chart after it
delivery_rate_end = """    <!-- Employee Count Section (DISABLED) -->"""

stats_chart_html = """    <!-- ============================================================
         VISUALIZATION: Trip Statistics Chart (Issue 4)
         ============================================================ -->
    <div class="section-block viz-section" id="statsChartSection">
        <div class="section-hdr">
            <span>&#9632;</span> تحليل إحصائيات الرحلات
        </div>
        <div class="section-body" style="padding: 14px;">
            <div style="display:flex; gap:16px; flex-wrap:wrap; align-items:flex-start;">
                <div style="flex:1; min-width:200px; max-width:260px; display:flex; align-items:center; justify-content:center;">
                    <canvas id="statsDonutChart" style="max-width:220px; max-height:220px;"></canvas>
                </div>
                <div style="flex:2; min-width:200px;">
                    <!-- KPI Cards -->
                    <div id="kpiCardsRow" style="display:grid; grid-template-columns:repeat(3,1fr); gap:10px; margin-bottom:14px;">
                        <div class="kpi-card" id="kpiTrips">
                            <div class="kpi-label">عدد الرحلات</div>
                            <div class="kpi-value" id="kpiTripsVal">0</div>
                        </div>
                        <div class="kpi-card" id="kpiPilgrims">
                            <div class="kpi-label">عدد الحجاج</div>
                            <div class="kpi-value" id="kpiPilgrimsVal">0</div>
                        </div>
                        <div class="kpi-card" id="kpiRate">
                            <div class="kpi-label">نسبة التفعيل</div>
                            <div class="kpi-value" id="kpiRateVal">0%</div>
                        </div>
                    </div>
                    <p id="statsChartEmpty" style="text-align:center;color:#aaa;font-size:11px;font-family:'Cairo',sans-serif;padding:10px 0; display:none;">
                        سيتم عرض الرسم البياني تلقائياً عند إدخال البيانات
                    </p>
                </div>
            </div>
        </div>
    </div>

    <!-- Employee Count Section (DISABLED) -->"""

content = content.replace(delivery_rate_end, stats_chart_html)

print("Issue 4 (stats chart placeholder) applied:", "statsDonutChart" in content)

# ============================================================
# Add KPI card CSS styles
# ============================================================

kpi_css = """
/* ============================================================
   KPI CARDS — for statistics visualization section
   ============================================================ */
.kpi-card {
    background: var(--primary-lighter);
    border: 1.5px solid var(--primary);
    border-radius: 8px;
    padding: 10px 8px;
    text-align: center;
    font-family: 'Cairo', sans-serif;
}
.kpi-label {
    font-size: calc(var(--body-size) - 0.5px);
    font-weight: 600;
    color: var(--primary-dark);
    margin-bottom: 4px;
}
.kpi-value {
    font-size: calc(var(--body-size) + 4px);
    font-weight: 800;
    color: var(--primary);
}

/* Visualization section container */
.viz-section .section-body canvas {
    display: block;
    margin: 0 auto;
}

"""

# Insert KPI CSS before the @media print block
content = content.replace("@media print {", kpi_css + "@media print {", 1)

print("KPI CSS applied:", ".kpi-card" in content)

# ============================================================
# ISSUE 5: Mobile responsiveness CSS
# ============================================================

mobile_css = """
/* ============================================================
   MOBILE RESPONSIVENESS — @media (max-width: 768px)
   ============================================================ */
@media (max-width: 768px) {
    /* Controls bar: scrollable row */
    .controls-bar {
        flex-wrap: nowrap;
        overflow-x: auto;
        padding: 10px 12px;
        gap: 10px;
        -webkit-overflow-scrolling: touch;
    }
    .controls-bar label { font-size: 11px; }
    .controls-bar select,
    .controls-bar input[type="date"] {
        min-width: 100px;
        font-size: 11px;
        padding: 5px 8px;
    }
    .btn-print {
        font-size: 12px;
        padding: 7px 14px;
        white-space: nowrap;
        flex-shrink: 0;
    }

    /* Report page: full viewport width */
    .report-page {
        width: 100vw !important;
        max-width: 100vw !important;
        margin: 0 !important;
        padding: 10px 8px !important;
        box-shadow: none !important;
        min-height: unset !important;
    }

    /* Header: stack vertically on very small screens */
    .report-header {
        flex-wrap: wrap;
        gap: 6px;
    }
    .header-side, .header-spacer {
        width: 100px;
        min-height: 50px;
    }
    .logo-img { width: 100px; max-height: 50px; }
    .header-center h1 { font-size: 12px !important; white-space: normal !important; }

    /* All tables: horizontally scrollable */
    .section-body { overflow-x: auto; padding: 6px 8px; }
    .journey-tbl, .case-tbl, .sub-tbl, .attend-tbl {
        min-width: 480px;
    }

    /* Bottom grid: single column */
    .bottom-grid { grid-template-columns: 1fr; }
    .grid-2 { grid-template-columns: 1fr; }

    /* KPI cards: 1 column on very small screens */
    #kpiCardsRow { grid-template-columns: 1fr !important; }

    /* Delivery rate: stack */
    .rate-display { flex-direction: column; align-items: center; }

    /* Font size adjustments */
    body { font-size: 12px; }
    .section-hdr { font-size: 13px; }
}

@media (max-width: 480px) {
    #kpiCardsRow { grid-template-columns: 1fr !important; }
    .report-header { flex-direction: column; align-items: center; }
    .header-spacer { display: none; }
}

"""

# Insert mobile CSS before the closing </style> tag
content = content.replace("</style>\n</head>", mobile_css + "</style>\n</head>", 1)

print("Issue 5 (mobile CSS) applied:", "@media (max-width: 768px)" in content)

# ============================================================
# Add Chart.js CDN and chart initialization JavaScript
# ============================================================

chart_js = """
/* ----------------------------------------------------------
   CHART.JS VISUALIZATIONS
   ---------------------------------------------------------- */

/* Load Chart.js from CDN dynamically */
(function loadChartJS() {
    if (typeof Chart !== 'undefined') { initCharts(); return; }
    var s = document.createElement('script');
    s.src = 'https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js';
    s.onload = function() { initCharts(); };
    document.head.appendChild(s);
})();

var _empChart = null;
var _statsChart = null;

function initCharts() {
    updateEmpChart();
    updateStatsChart();
}

/* ----------------------------------------------------------
   EMPLOYEE DISTRIBUTION CHART (horizontal bar)
   ---------------------------------------------------------- */
function updateEmpChart() {
    if (typeof Chart === 'undefined') return;

    var rows = document.querySelectorAll('#caseBody tr');
    var empData = {};
    rows.forEach(function(r) {
        var empField = r.querySelector('.searchable-field');
        var inputs = r.querySelectorAll('input[type="number"]');
        if (!empField || empField.classList.contains('placeholder-text') || empField.classList.contains('empty')) return;
        var empName = (empField.dataset.value || empField.textContent || '').trim();
        if (!empName) return;
        var cards = parseInt(inputs[0] ? inputs[0].value : 0) || 0;
        var activated = parseInt(inputs[1] ? inputs[1].value : 0) || 0;
        var notActivated = parseInt(inputs[2] ? inputs[2].value : 0) || 0;
        if (!empData[empName]) empData[empName] = { cards: 0, activated: 0, notActivated: 0 };
        empData[empName].cards += cards;
        empData[empName].activated += activated;
        empData[empName].notActivated += notActivated;
    });

    var empNames = Object.keys(empData);
    var canvas = document.getElementById('empDistChart');
    var emptyMsg = document.getElementById('empChartEmpty');

    if (empNames.length === 0) {
        if (canvas) canvas.style.display = 'none';
        if (emptyMsg) emptyMsg.style.display = 'block';
        if (_empChart) { _empChart.destroy(); _empChart = null; }
        return;
    }

    if (canvas) canvas.style.display = 'block';
    if (emptyMsg) emptyMsg.style.display = 'none';

    var labels = empNames;
    var cardsData    = empNames.map(function(n){ return empData[n].cards; });
    var activatedData = empNames.map(function(n){ return empData[n].activated; });
    var notActData   = empNames.map(function(n){ return empData[n].notActivated; });

    if (_empChart) { _empChart.destroy(); }

    var ctx = canvas.getContext('2d');
    _empChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [
                {
                    label: 'بطاقات مفوضة',
                    data: cardsData,
                    backgroundColor: '#2D7D6F',
                    borderRadius: 4,
                    borderSkipped: false
                },
                {
                    label: 'تم التفعيل',
                    data: activatedData,
                    backgroundColor: '#3A9B8A',
                    borderRadius: 4,
                    borderSkipped: false
                },
                {
                    label: 'لم يتم التفعيل',
                    data: notActData,
                    backgroundColor: '#A8D5CC',
                    borderRadius: 4,
                    borderSkipped: false
                }
            ]
        },
        options: {
            indexAxis: 'y',
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'top',
                    labels: {
                        font: { family: 'Cairo', size: 11 },
                        color: '#1A1A1A'
                    }
                },
                tooltip: {
                    callbacks: {
                        label: function(ctx) {
                            return ctx.dataset.label + ': ' + ctx.parsed.x;
                        }
                    }
                }
            },
            scales: {
                x: {
                    beginAtZero: true,
                    ticks: { font: { family: 'Cairo', size: 10 }, color: '#444' },
                    grid: { color: 'rgba(0,0,0,0.06)' }
                },
                y: {
                    ticks: { font: { family: 'Cairo', size: 10 }, color: '#444' }
                }
            }
        }
    });

    /* Adjust canvas height based on number of employees */
    canvas.parentElement.style.height = Math.max(200, empNames.length * 60 + 80) + 'px';
}

/* ----------------------------------------------------------
   STATISTICS DONUT CHART
   ---------------------------------------------------------- */
function updateStatsChart() {
    if (typeof Chart === 'undefined') return;

    var returned     = parseInt(document.getElementById('cardsReturned').value) || 0;
    var lost         = parseInt(document.getElementById('cardsLost').value) || 0;
    var transferred  = parseInt(document.getElementById('cardsTransferred').value) || 0;
    var trips        = parseInt(document.getElementById('tripsCount').value) || 0;
    var pilgrims     = parseInt(document.getElementById('pilgrimsCount').value) || 0;
    var rateText     = document.getElementById('ratePercent') ? document.getElementById('ratePercent').textContent : '0%';

    /* Update KPI cards */
    document.getElementById('kpiTripsVal').textContent    = trips;
    document.getElementById('kpiPilgrimsVal').textContent = pilgrims;
    document.getElementById('kpiRateVal').textContent     = rateText;

    var canvas = document.getElementById('statsDonutChart');
    var total = returned + lost + transferred;

    if (total === 0) {
        if (_statsChart) { _statsChart.destroy(); _statsChart = null; }
        if (canvas) canvas.style.display = 'none';
        return;
    }

    if (canvas) canvas.style.display = 'block';

    if (_statsChart) { _statsChart.destroy(); }

    var ctx = canvas.getContext('2d');
    _statsChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['بطاقات مسترجعة', 'بطاقات مفقودة', 'بطاقات محولة'],
            datasets: [{
                data: [returned, lost, transferred],
                backgroundColor: ['#2D7D6F', '#E74C3C', '#F39C12'],
                borderColor: ['#1B5E50', '#C0392B', '#D68910'],
                borderWidth: 2,
                hoverOffset: 8
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            cutout: '60%',
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: {
                        font: { family: 'Cairo', size: 10 },
                        color: '#1A1A1A',
                        padding: 8
                    }
                },
                tooltip: {
                    callbacks: {
                        label: function(ctx) {
                            var pct = total > 0 ? Math.round(ctx.parsed / total * 100) : 0;
                            return ctx.label + ': ' + ctx.parsed + ' (' + pct + '%)';
                        }
                    }
                }
            }
        },
        plugins: [{
            id: 'centerText',
            afterDraw: function(chart) {
                var ctx2 = chart.ctx;
                var cx = chart.chartArea.left + (chart.chartArea.right - chart.chartArea.left) / 2;
                var cy = chart.chartArea.top + (chart.chartArea.bottom - chart.chartArea.top) / 2;
                ctx2.save();
                ctx2.font = 'bold 13px Cairo, sans-serif';
                ctx2.fillStyle = '#2D7D6F';
                ctx2.textAlign = 'center';
                ctx2.textBaseline = 'middle';
                ctx2.fillText('الإجمالي', cx, cy - 8);
                ctx2.font = 'bold 16px Cairo, sans-serif';
                ctx2.fillText(total, cx, cy + 10);
                ctx2.restore();
            }
        }]
    });
}

"""

# Insert chart JS before the closing </script> tag
content = content.replace("</script>\n</body>", chart_js + "\n</script>\n</body>", 1)

print("Chart.js code applied:", "updateEmpChart" in content)

# ============================================================
# Hook updateEmpChart and updateStatsChart into existing functions
# ============================================================

# Hook into updateEmpSummary to also update the chart
old_update_emp_summary_end = """    empNames.forEach(function(name) {
        var d = empData[name];
        var tr = document.createElement('tr');
        tr.innerHTML =
            '<td style="text-align:center;padding:4px 6px;line-height:1.4;word-break:break-word;">' + escapeHTML(name) + '</td>' +
            '<td style="text-align:center;padding:4px 6px;">' + d.cards + '</td>' +
            '<td style="text-align:center;padding:4px 6px;">' + d.activated + '</td>' +
            '<td style="text-align:center;padding:4px 6px;">' + d.notActivated + '</td>';
        tbody.appendChild(tr);
    });
}"""

new_update_emp_summary_end = """    empNames.forEach(function(name) {
        var d = empData[name];
        var tr = document.createElement('tr');
        tr.innerHTML =
            '<td style="text-align:center;padding:4px 6px;line-height:1.4;word-break:break-word;">' + escapeHTML(name) + '</td>' +
            '<td style="text-align:center;padding:4px 6px;">' + d.cards + '</td>' +
            '<td style="text-align:center;padding:4px 6px;">' + d.activated + '</td>' +
            '<td style="text-align:center;padding:4px 6px;">' + d.notActivated + '</td>';
        tbody.appendChild(tr);
    });

    /* Update employee distribution chart */
    if (typeof updateEmpChart === 'function') updateEmpChart();
}"""

content = content.replace(old_update_emp_summary_end, new_update_emp_summary_end)

# Hook into calcDeliveryRate to update stats chart
old_calc_rate_end = """    document.getElementById('rateCircle').style.background    =
        'conic-gradient(var(--primary) 0% ' + pct + '%, #e0e0e0 ' + pct + '% 100%)';
    updateEmpSummary();
    autoDetectStats();
}"""

new_calc_rate_end = """    document.getElementById('rateCircle').style.background    =
        'conic-gradient(var(--primary) 0% ' + pct + '%, #e0e0e0 ' + pct + '% 100%)';
    updateEmpSummary();
    autoDetectStats();

    /* Update statistics chart */
    if (typeof updateStatsChart === 'function') updateStatsChart();
}"""

content = content.replace(old_calc_rate_end, new_calc_rate_end)

# Also hook stats chart update when stats inputs change
old_cards_returned = """<input type="number" placeholder="0" min="0" id="cardsReturned">"""
new_cards_returned = """<input type="number" placeholder="0" min="0" id="cardsReturned" oninput="if(typeof updateStatsChart==='function')updateStatsChart();">"""
content = content.replace(old_cards_returned, new_cards_returned)

old_cards_lost = """<input type="number" placeholder="0" min="0" id="cardsLost">"""
new_cards_lost = """<input type="number" placeholder="0" min="0" id="cardsLost" oninput="if(typeof updateStatsChart==='function')updateStatsChart();">"""
content = content.replace(old_cards_lost, new_cards_lost)

old_cards_transferred = """<input type="number" placeholder="0" min="0" id="cardsTransferred">"""
new_cards_transferred = """<input type="number" placeholder="0" min="0" id="cardsTransferred" oninput="if(typeof updateStatsChart==='function')updateStatsChart();">"""
content = content.replace(old_cards_transferred, new_cards_transferred)

print("Chart hooks applied:", "updateEmpChart" in content and "updateStatsChart" in content)

# ============================================================
# Write the final file
# ============================================================

with open('/home/ubuntu/report_project/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("\\nAll enhancements applied successfully!")
print("Final file size:", len(content), "chars")
