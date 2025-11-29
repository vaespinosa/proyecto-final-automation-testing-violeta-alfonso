import pytest
from utils.screenshot import take_screenshot

pytest_html = None

def pytest_configure(config):
    global pytest_html
    pytest_html = config.pluginmanager.getplugin('html')

def pytest_html_report_title(report):
    report.title = "Reporte de Pruebas Automatizadas"

def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([
        "<p><strong>Proyecto:</strong> Framework Automatización</p>",
        "<p><strong>Autor:</strong> Violeta Alfonso</p>",
        "<p><strong>Curso:</strong> Testing Automation</p>",
        "<p><strong>Fecha:</strong> 2025-11-28</p>"
    ])

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver", None)
        if driver and pytest_html:
            test_name = item.name
            screenshot_path = take_screenshot(driver, test_name)
            import os
            rel_path = os.path.relpath(screenshot_path, os.path.dirname(item.config.option.htmlpath or 'report.html'))
            extra = getattr(rep, "extra", None)
            if extra is None:
                extra = []
            extra.append(pytest_html.extras.image(screenshot_path, mime_type='image/png', extension='png'))
            rep.extra = extra
