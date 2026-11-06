# Predictive maintenance on NASA C-MAPSS

We are Team Thinkers, two students from NSUT. This is our project for TELIPORT Season 4 (Tata Elxsi), Case Study 1.

The problem: machines in a fleet keep sending sensor data, but failures are usually noticed only after a breakdown. We want to build a system that reads the sensor data, spots early signs of wear, estimates how many cycles a machine has left, and creates a maintenance work order on its own. A person only steps in when something looks unusual.

We are using the NASA C-MAPSS turbofan engine dataset. We start with FD001 and move to FD002, FD003 and FD004 later.

This is still being built, so most of it doesn't exist yet. The checklist below shows where we are.

## What we plan to build

- Data cleaning and rolling-window features
- An anomaly score (how far an engine is from healthy)
- A model that predicts remaining useful life (RUL)
- A simple rule-based agent (no LLM) that turns the results into work orders
- MLflow to track experiments, plus a small API and a Streamlit dashboard

## Progress

- [x] Repo and folder structure
- [ ] Load and explore FD001
- [ ] RUL labels, baseline and metrics
- [ ] Cleaning and features
- [ ] RUL model
- [ ] Anomaly score
- [ ] Agent and work orders
- [ ] MLflow and experiments
- [ ] API and dashboard
- [ ] Retraining, drift check and Docker
- [ ] FD002 to FD004

## Data

The NASA files are not stored in this repo. Download C-MAPSS from [NASA's data page](https://data.nasa.gov/dataset/cmapss-jet-engine-simulated-data) and put the files in the `data/` folder.

## How to run

Nothing to run yet. We will add the steps once the pipeline works.