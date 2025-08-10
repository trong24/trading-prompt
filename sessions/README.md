# Sessions Folder

Each session is a pair of files:
- `YYYY-MM-DD_NN.session.json`  (exact input you gave to the model)
- `YYYY-MM-DD_NN.output.json`   (your actual plan/decision — ground truth)

## Session JSON schema (input)
```json
{
  "session": {"date":"YYYY-MM-DD","tz":"+07:00","mode":"scan|review"},
  "account": {"venue":"Binance","instrument":"BTCUSDT","type":"perp","leverage":5,"margin_mode":"cross"},
  "constraints": {"max_new_trades": 1, "skip_if_news_risk": true},
  "market": {
    "btc_brief": "…",
    "volatility": "…",
    "funding_open_interest": "…",
    "calendar": "…"
  },
  "levels": {"support":[...], "resistance":[...]},
  "signals": {"ma":{"20":"up","50":"flat","200":"up"}, "rsi_14": 55, "atr": 1200, "volume": "…", "structure": "…"},
  "notes": "…",
  "positions": [{"side":"long","avg_price":..., "qty":..., "stop":..., "thesis":"…"}],
  "nav_usdt": 10000
}
```

## Output JSON schema (ground truth)
The output you *actually* executed (entry/stop/targets/size/logic). Keep consistent.
