# dvc-demo
DVC demo for IVADO Labs bi-weekly DE/DS meeting

# Demo content
- [Deck](https://docs.google.com/presentation/d/1G661owf_hLazZ5oyAzNoXq7EVpw7hylUMB6ThF27u88/edit#slide=id.p) presentation (up to demo)
- Demo
  - Overview of `dvc.yaml`
  - Usage of `dvc status`
  - Modify the model
    - `dvc exp run --set-param model.num_hidden_layer=24`
    - Create and new branch and checkout
    - Git push
    - CI/CD explications
- Good practices
- Conclusion
- [Extra] GTO (Git Tag Ops)
  - `gto register neural-net`
  - `gto show`
  - `gto assign neural-net --stage dev`
  - `git push origin neural-net@v0.1.1`