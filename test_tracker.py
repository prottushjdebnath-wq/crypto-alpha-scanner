from app.paper.tracker import PaperTracker

tracker = PaperTracker()

tracker.record(
    symbol="BTCUSDT",
    side="LONG",
    score=92,
    entry=65000,
    stop_loss=64000,
    take_profit=68000
)

print("Paper trade recorded")
