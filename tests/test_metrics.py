from robogenma.utils.metrics import make_metrics


def test_make_metrics_success_case():
    planned = [(0, 0), (1, 0), (2, 0)]
    executed = [(0, 0), (1, 0), (2, 0)]
    m = make_metrics(planned, executed, max_steps=100)
    assert m.success is True
    assert m.completion_rate == 1.0
    assert m.localization_error == 0.0

