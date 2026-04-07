# RobogenMA Streamlit MVP

RobogenMA is a lightweight end-to-end demo for:

`Task Input -> RK parsing -> CS strategy -> 2D simulation -> FO optimization -> report`

## 1) Quick start (local)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## 2) Project structure

- `app.py`: Streamlit entry page
- `pages/`: core pages (`Task Input`, `Parameter Table`, `Simulation`, `Report`)
- `robogenma/agents/`: `MainAgent`, `RKAgent`, `CSAgent`, `FOAgent`
- `robogenma/sim/`: 2D grid environment, improved A* planner, simulation engine
- `robogenma/schemas/`: Pydantic models for requests, results, metrics
- `robogenma/utils/`: metrics, report export, visualization, seed helpers
- `data/examples/`: fixed demo scenarios
- `tests/`: minimal smoke + unit tests

## 3) Demo scenarios

- `data/examples/simple_task.json`
- `data/examples/complex_task.json`

Both use deterministic defaults for stable classroom demos.

## 4) Tests

```bash
pytest -q
```

## 5) Deployment (Streamlit Community Cloud)

1. Push this project to a GitHub repository.
2. Open [Streamlit Community Cloud](https://share.streamlit.io/).
3. Create app and set:
   - **Main file path**: `app.py`
   - **Python version**: `3.11`
4. Deploy and wait for build completion.
5. Copy generated public URL and place it below.

### Online demo URL

- `TBD_AFTER_DEPLOY`

### 3-minute demo script

1. Open homepage, explain RK-CS-Sim-FO pipeline.
2. Load `simple_task` on Task Input page and save.
3. Show parsed table on Parameter page.
4. Run Simulation with fixed seed `42`.
5. Show Report metrics + feedback, then download markdown report.

## 6) Known limitations

- Uses lightweight 2D grid simulation (no PyBullet/COMSOL yet).
- Disturbance execution model is deterministic for repeatability.
- Planner interface is designed for future replacement by real physics engine.

