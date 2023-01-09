# dvc-demo
DVC demo for IVADO Labs bi-weekly DE/DS meeting

# Demo content
- [Deck](https://docs.google.com/presentation/d/1G661owf_hLazZ5oyAzNoXq7EVpw7hylUMB6ThF27u88/edit#slide=id.p) presentation (up to demo)
- Demo
  - Overview of `dvc.yaml`
  - Usage of `dvc status`
  - Modify the model
    - `dvc exp run --set-param model.num_hidden_layer=24`
    - `dvc exp show`
    - `dvc exp branch nn-hl24 "nn-hidden-layer-24"`
    - `dvc push`
    - `git push -u origin features/nn-hl24`
- Good practices
- Conclusion
- Extra: GTO
