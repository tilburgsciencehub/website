
from flask import redirect, url_for

def setup_redirects(app):
    @app.route('/building-blocks/collaborate-and-share-your-work/write-your-paper/plotnine-altair/')
    def redirect_0():
        return redirect(url_for('home', _external=True) + "topics/visualization/data-visualization/graphs-charts/plotnine-altair/", code=301)

    @app.route('/building-blocks/develop-your-research-skills/tips/stata-code-style/')
    def redirect_1():
        return redirect(url_for('home', _external=True) + "topics/computer-setup/software-installation/stata/stata-code-style/", code=301)

    @app.route('/building-blocks/analyze-data/regressions/model-assumptions/')
    def redirect_2():
        return redirect(url_for('home', _external=True) + "topics/analyze/regression/reporting/model-assumptions/", code=301)

    @app.route('/building-blocks/analyze-data/regression-discontinuity/continuity-approach/')
    def redirect_3():
        return redirect(url_for('home', _external=True) + "topics/analyze/causal-inference/rdd/continuity-approach/", code=301)

    @app.route('/tutorials/more-tutorials/write-your-first-latex-document/')
    def redirect_4():
        return redirect(url_for('home', _external=True) + "topics/research-skills/templates-dynamic-content/templates/write-your-first-latex-document/", code=301)

    @app.route('/building-blocks/prepare-your-data-for-analysis/data-preparation/large-datasets-r/')
    def redirect_5():
        return redirect(url_for('home', _external=True) + "topics/manage-manipulate/loading/large-datasets/large-datasets-r/", code=301)

    @app.route('/building-blocks/automate-and-execute-your-work/automate-your-workflow/remake/')
    def redirect_6():
        return redirect(url_for('home', _external=True) + "topics/automation/automation-tools/makefiles/remake/", code=301)

    @app.route('/building-blocks/collaborate-and-share-your-work/publish-on-the-web/using-r/')
    def redirect_7():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/share-your-work/content-creation/using-r/", code=301)

    @app.route('/building-blocks/collaborate-and-share-your-work/use-github/versioning-using-git/')
    def redirect_8():
        return redirect(url_for('home', _external=True) + "topics/automation/version-control/start-git/versioning-using-git/", code=301)

    @app.route('/building-blocks/automate-and-execute-your-work/automate-your-workflow/what-are-makefiles/')
    def redirect_9():
        return redirect(url_for('home', _external=True) + "topics/automation/automation-tools/makefiles/what-are-makefiles/", code=301)

    @app.route('/building-blocks/collaborate-and-share-your-work/write-your-paper/latex-templates/')
    def redirect_10():
        return redirect(url_for('home', _external=True) + "topics/research-skills/templates-dynamic-content/templates/latex-templates/", code=301)

    @app.route('/building-blocks/configure-your-computer/statistics-and-computation/perl/')
    def redirect_11():
        return redirect(url_for('home', _external=True) + "topics/computer-setup/software-installation/perl/perl/", code=301)

    @app.route('/building-blocks/analyze-data/regression-discontinuity/impact-evaluation/')
    def redirect_12():
        return redirect(url_for('home', _external=True) + "topics/analyze/causal-inference/did/impact-evaluation/", code=301)

    @app.route('/building-blocks/analyze-data/regressions/impact-evaluation/')
    def redirect_13():
        return redirect(url_for('home', _external=True) + "topics/analyze/causal-inference/did/impact-evaluation/", code=301)

    @app.route('/building-blocks/share-your-results-and-project/use-github/git-lfs/')
    def redirect_14():
        return redirect(url_for('home', _external=True) + "topics/automation/version-control/advanced-git/git-lfs/", code=301)

    @app.route('/building-blocks/collaborate-and-share-your-work/use-github/naming-git-branches/')
    def redirect_15():
        return redirect(url_for('home', _external=True) + "topics/automation/version-control/advanced-git/naming-git-branches/", code=301)

    @app.route('/building-blocks/collaborate-and-share-your-work/project_management/team-transition/')
    def redirect_16():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/project-management/big-team-science/team-transition/", code=301)

    @app.route('/building-blocks/analyze-data/regressions/interaction-terms-r/')
    def redirect_17():
        return redirect(url_for('home', _external=True) + "topics/analyze/regression/linear-regression/interaction-terms-r/", code=301)

    @app.route('/building-blocks/configure-your-computer/statistics-and-computation/stata/')
    def redirect_18():
        return redirect(url_for('home', _external=True) + "topics/computer-setup/software-installation/stata/stata/", code=301)

    @app.route('/tutorials/reproducible-research-and-automation/practicing-pipeline-automation-make/modifications/')
    def redirect_19():
        return redirect(url_for('home', _external=True) + "topics/automation/automation-tools/makefiles/practicing-pipeline-automation-make/modifications/", code=301)

    @app.route('/tutorials/more-tutorials/airbnb-workflow/')
    def redirect_20():
        return redirect(url_for('home', _external=True) + "topics/automation/automation-tools/makefiles/airbnb-workflow/", code=301)

    @app.route('/building-blocks/collaborate-and-share-your-work/project_management/meeting_preparation/')
    def redirect_21():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/project-management/big-team-science/meeting_preparation/", code=301)

    @app.route('/building-blocks/configure-your-computer/infrastructure-choice/configure-git/')
    def redirect_22():
        return redirect(url_for('home', _external=True) + "topics/automation/replicability/cloud-computing/configure-git/", code=301)

    @app.route('/building-blocks/prepare-your-data-for-analysis/data-preparation/clean-social-media-counts/')
    def redirect_23():
        return redirect(url_for('home', _external=True) + "topics/manage-manipulate/manipulate-clean/numerical/clean-social-media-counts/", code=301)

    @app.route('/tutorials/code-like-a-pro/github-copilot/')
    def redirect_24():
        return redirect(url_for('home', _external=True) + "topics/automation/ai/gpt-models/github-copilot/", code=301)

    @app.route('/building-blocks/collaborate-and-share-your-work/write-your-paper/research-paper-lyx/')
    def redirect_25():
        return redirect(url_for('home', _external=True) + "topics/research-skills/templates-dynamic-content/templates/research-paper-lyx/", code=301)

    @app.route('/building-blocks/configure-your-computer/automation-and-workflows/snakemake/')
    def redirect_26():
        return redirect(url_for('home', _external=True) + "topics/automation/automation-tools/makefiles/snakemake/", code=301)

    @app.route('/building-blocks/analyze-data/regressions/modelplot/')
    def redirect_27():
        return redirect(url_for('home', _external=True) + "topics/visualization/data-visualization/regression-results/modelplot/", code=301)

    @app.route('/building-blocks/collect-data/workflows-for-online-data-collection/monitor-data-quality/')
    def redirect_28():
        return redirect(url_for('home', _external=True) + "topics/collect-store/data-collection/web-scraping/monitor-data-quality/", code=301)

    @app.route('/building-blocks/configure-your-computer/infrastructure-choice/lisa_cluster/')
    def redirect_29():
        return redirect(url_for('home', _external=True) + "topics/automation/replicability/cloud-computing/lisa_cluster/", code=301)

    @app.route('/tutorials/reproducible-research-and-automation/practicing-pipeline-automation-make/clone/')
    def redirect_30():
        return redirect(url_for('home', _external=True) + "topics/automation/automation-tools/makefiles/practicing-pipeline-automation-make/clone/", code=301)

    @app.route('/building-blocks/collaborate-and-share-your-work/use-github/make-code-citable-with-doi/')
    def redirect_31():
        return redirect(url_for('home', _external=True) + "topics/automation/version-control/repository-lifecycle/make-code-citable-with-doi/", code=301)

    @app.route('/tutorials/reproducible-research-and-automation/practicing-pipeline-automation-make/pipeline-make/')
    def redirect_32():
        return redirect(url_for('home', _external=True) + "topics/automation/automation-tools/makefiles/practicing-pipeline-automation-make/pipeline-make/", code=301)

    @app.route('/building-blocks/analyze-data/regressions/interpreting-regression-models-r/')
    def redirect_33():
        return redirect(url_for('home', _external=True) + "topics/analyze/regression/linear-regression/interpreting-regression-models-r/", code=301)

    @app.route('/tutorials/reproducible-research-and-automation/principles-of-project-setup-and-workflow-management/directories/')
    def redirect_34():
        return redirect(url_for('home', _external=True) + "topics/automation/workflows/starting/principles-of-project-setup-and-workflow-management/directories/", code=301)

    @app.route('/building-blocks/configure-your-computer/statistics-and-computation/python/')
    def redirect_35():
        return redirect(url_for('home', _external=True) + "topics/computer-setup/software-installation/python/", code=301)

    @app.route('/building-blocks/collaborate-and-share-your-work/use-github/git-branching-strategies/')
    def redirect_36():
        return redirect(url_for('home', _external=True) + "topics/automation/version-control/advanced-git/git-branching-strategies/", code=301)

    @app.route('/building-blocks/configure-your-computer/task-specific-configurations/configuring-python-for-webscraping/')
    def redirect_37():
        return redirect(url_for('home', _external=True) + "topics/computer-setup/software-installation/python/configuring-python-for-webscraping/", code=301)

    @app.route('/building-blocks/analyze-data/regressions/mediation-analysis/')
    def redirect_38():
        return redirect(url_for('home', _external=True) + "topics/analyze/regression/linear-regression/mediation-analysis/", code=301)

    @app.route('/tutorials/more-tutorials/contribute-to-tilburg-science-hub/')
    def redirect_39():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/project-management/contribute-to-tilburg-science-hub/", code=301)

    @app.route('/tutorials/code-like-a-pro/getting-started-with-r/getting-started-with-r-overview/')
    def redirect_40():
        return redirect(url_for('home', _external=True) + "topics/computer-setup/software-installation/rstudio/getting-started-with-r-overview/", code=301)

    @app.route('/building-blocks/analyze-data/machine-learning/xgboost/')
    def redirect_41():
        return redirect(url_for('home', _external=True) + "topics/analyze/machine-learning/supervised/xgboost/", code=301)

    @app.route('/building-blocks/configure-your-computer/statistics-and-computation/git/')
    def redirect_42():
        return redirect(url_for('home', _external=True) + "topics/automation/version-control/start-git/git/", code=301)

    @app.route('/building-blocks/collaborate-and-share-your-work/write-your-paper/forest-plot-generation-r/')
    def redirect_43():
        return redirect(url_for('home', _external=True) + "topics/visualization/data-visualization/regression-results/forest-plot-generation-r/", code=301)

    @app.route('/building-blocks/collaborate-and-share-your-work/use-github/remove-files/')
    def redirect_44():
        return redirect(url_for('home', _external=True) + "topics/automation/version-control/advanced-git/remove-files/", code=301)

    @app.route('/building-blocks/automate-and-execute-your-work/automate-your-workflow/intro_ghactions/')
    def redirect_45():
        return redirect(url_for('home', _external=True) + "topics/automation/automation-tools/deployment/intro_ghactions/", code=301)

    @app.route('/tutorials/reproducible-research-and-automation/principles-of-project-setup-and-workflow-management/project-setup-overview/')
    def redirect_46():
        return redirect(url_for('home', _external=True) + "topics/automation/workflows/starting/principles-of-project-setup-and-workflow-management/project-setup-overview/", code=301)

    @app.route('/workflow/documenting-data')
    def redirect_47():
        return redirect(url_for('home', _external=True) + "topics/automation/workflows/starting/principles-of-project-setup-and-workflow-management/documenting-data/", code=301)

    @app.route('/building-blocks/develop-your-research-skills/tips/citations/')
    def redirect_48():
        return redirect(url_for('home', _external=True) + "topics/research-skills/writing/citations/", code=301)

    @app.route('/building-blocks/collaborate-and-share-your-work/write-your-paper/export-tables/')
    def redirect_49():
        return redirect(url_for('home', _external=True) + "topics/visualization/reporting-tables/reportingtables/export-tables/", code=301)

    @app.route('/tutorials/code-like-a-pro/hugo-website/pick-theme/')
    def redirect_50():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/share-your-work/content-creation/hugo-website/pick-theme/", code=301)

    @app.route('/building-blocks/collaborate-and-share-your-work/write-your-paper/tisemdown_thesis_template.pdf')
    def redirect_51():
        return redirect(url_for('home', _external=True) + "topics/research-skills/templates-dynamic-content/templates/tisemdown_thesis_template.pdf", code=301)

    @app.route('/building-blocks/analyze-data/regressions/marginal-effect-r/')
    def redirect_52():
        return redirect(url_for('home', _external=True) + "topics/analyze/regression/linear-regression/marginal-effect-r/", code=301)

    @app.route('/topics/configure-your-computer/automation-and-workflows/environment-variables/')
    def redirect_53():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/project-management/project-management-gh/environment-variables/", code=301)

    @app.route('/tutorials/code-like-a-pro/web-scraping/web-scraping-tutorial/')
    def redirect_54():
        return redirect(url_for('home', _external=True) + "topics/collect-store/data-collection/web-scraping/web-scraping-tutorial/", code=301)

    @app.route('/building-blocks/collect-data/webscraping-apis/avoid-getting-blocked/')
    def redirect_55():
        return redirect(url_for('home', _external=True) + "topics/collect-store/data-collection/web-scraping/avoid-getting-blocked/", code=301)

    @app.route('/building-blocks/automate-and-execute-your-work/automate-your-workflow/ghactions-workflow/')
    def redirect_56():
        return redirect(url_for('home', _external=True) + "topics/automation/automation-tools/deployment/ghactions-workflow/", code=301)

    @app.route('/tutorials/educational-support/educational-videos/equipment-edu-videos/')
    def redirect_57():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/share-your-work/content-creation/educational-videos/equipment-edu-videos/", code=301)

    @app.route('/building-blocks/configure-your-computer/automation-and-workflows/awscli/')
    def redirect_58():
        return redirect(url_for('home', _external=True) + "topics/automation/replicability/cloud-computing/awscli/", code=301)

    @app.route('/building-blocks/develop-your-research-skills/tips/search-literature/')
    def redirect_59():
        return redirect(url_for('home', _external=True) + "topics/research-skills/writing/literature-review/search-literature/", code=301)

    @app.route('/building-blocks/analyze-data/regressions-paneldata/staggered-did/')
    def redirect_60():
        return redirect(url_for('home', _external=True) + "topics/analyze/causal-inference/did/staggered-did/", code=301)

    @app.route('/building-blocks/analyze-data/regression-discontinuity/local-randomization/')
    def redirect_61():
        return redirect(url_for('home', _external=True) + "topics/analyze/causal-inference/rdd/local-randomization/", code=301)

    @app.route('/building-blocks/automate-and-execute-your-work/automate-your-workflow/tablefill/')
    def redirect_62():
        return redirect(url_for('home', _external=True) + "topics/visualization/reporting-tables/reportingtables/tablefill/", code=301)

    @app.route('/tutorials/more-tutorials/educational-videos/')
    def redirect_63():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/share-your-work/content-creation/educational-videos/", code=301)

    @app.route('/tutorials/reproducible-research-and-automation/practicing-pipeline-automation-make/')
    def redirect_64():
        return redirect(url_for('home', _external=True) + "topics/automation/automation-tools/makefiles/practicing-pipeline-automation-make/", code=301)

    @app.route('/tutorials/reproducible-research-and-automation/start-new-project/starting-up-a-new-project/')
    def redirect_65():
        return redirect(url_for('home', _external=True) + "topics/automation/workflows/starting/starting-up-a-new-project/", code=301)

    @app.route('/building-blocks/analyze-data/regressions-paneldata/canonical-did-regression/')
    def redirect_66():
        return redirect(url_for('home', _external=True) + "topics/analyze/causal-inference/did/canonical-did-regression/", code=301)

    @app.route('/building-blocks/analyze-data/regression-discontinuity/fuzzy-rdd/')
    def redirect_67():
        return redirect(url_for('home', _external=True) + "topics/analyze/causal-inference/rdd/fuzzy-rdd/", code=301)

    @app.route('/tutorials/project-management/scrum-for-researchers/use-scrum-in-your-team/')
    def redirect_68():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/project-management/big-team-science/use-scrum-in-your-team/", code=301)

    @app.route('/building-blocks/prepare-your-data-for-analysis/data-visualization/theory-best-practices/')
    def redirect_69():
        return redirect(url_for('home', _external=True) + "topics/visualization/data-visualization/graphs-charts/theory-best-practices/", code=301)

    @app.route('/building-blocks/automate-and-execute-your-work/automate-your-workflow/tsh_make_cheatsheet.pdf')
    def redirect_70():
        return redirect(url_for('home', _external=True) + "topics/automation/automation-tools/makefiles/images/tsh_make_cheatsheet.pdf", code=301)

    @app.route('/topics/collaborate-and-share-your-work/publish-on-the-web/using-r/')
    def redirect_71():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/share-your-work/content-creation/using-r/", code=301)

    @app.route('/topics/collaborate-and-share-your-work/publish-on-the-web/shiny-apps/')
    def redirect_72():
        return redirect(url_for('home', _external=True) + "topics/visualization/data-visualization/dashboarding/shiny-apps/", code=301)

    @app.route('/topics/automate-and-execute-your-work/automate-your-workflow/auto-install-r-packages/')
    def redirect_73():
        return redirect(url_for('home', _external=True) + "topics/automation/replicability/package-management/auto-install-r-packages/", code=301)

    @app.route('/tutorials/reproducible-research-and-automation/principles-of-project-setup-and-workflow-management/documenting-data/')
    def redirect_74():
        return redirect(url_for('home', _external=True) + "topics/automation/workflows/starting/principles-of-project-setup-and-workflow-management/documenting-data/", code=301)

    @app.route('/topics/analyze-data/regressions/synth-control/')
    def redirect_75():
        return redirect(url_for('home', _external=True) + "topics/analyze/causal-inference/did/synth-control/", code=301)

    @app.route('/tutorials/scale-up/running-computations-remotely/cloud-computing/')
    def redirect_76():
        return redirect(url_for('home', _external=True) + "topics/automation/replicability/cloud-computing/running-computations-remotely/cloud-computing/", code=301)

    @app.route('/tutorials/more-tutorials/contribute-to-tilburg-science-hub/style-guide/')
    def redirect_77():
        return redirect(url_for('home', _external=True) + "topics/Collaborate-share/Project-management/contribute-to-tilburg-science-hub/style-guide/", code=301)

    @app.route('/tutorials/more-tutorials/write-an-academic-paper/')
    def redirect_78():
        return redirect(url_for('home', _external=True) + "topics/research-skills/writing/writing-process/write-an-academic-paper/", code=301)

    @app.route('/tutorials/scale-up/running-computations-remotely/move-files/')
    def redirect_79():
        return redirect(url_for('home', _external=True) + "topics/automation/replicability/cloud-computing/running-computations-remotely/move-files/", code=301)

    @app.route('/tutorials/code-like-a-pro/hugo-website/get-hugo/')
    def redirect_80():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/share-your-work/content-creation/hugo-website/get-hugo/", code=301)

    @app.route('/building-blocks/collaborate-and-share-your-work/use-github/github_cheatsheet_tsh.pdf')
    def redirect_81():
        return redirect(url_for('home', _external=True) + "topics/automation/version-control/start-git/images/github_cheatsheet_tsh.pdf", code=301)

    @app.route('/building-blocks/collaborate-and-share-your-work/use-github/github-workflow/')
    def redirect_82():
        return redirect(url_for('home', _external=True) + "topics/automation/version-control/start-git/github-workflow/", code=301)

    @app.route('/tutorials/scale-up/running-computations-remotely/run-scripts/')
    def redirect_83():
        return redirect(url_for('home', _external=True) + "topics/automation/replicability/cloud-computing/running-computations-remotely/run-scripts/", code=301)

    @app.route('/tutorials/more-tutorials/educational-videos/shooting-edu-videos/')
    def redirect_84():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/share-your-work/content-creation/educational-videos/shooting-edu-videos/", code=301)

    @app.route('/topics/analyze-data/regressions/impact-evaluation')
    def redirect_85():
        return redirect(url_for('home', _external=True) + "topics/analyze/causal-inference/did/impact-evaluation/", code=301)

    @app.route('/topics/automate-and-execute-your-work/automate-your-workflow/stata-error-handling-make/')
    def redirect_86():
        return redirect(url_for('home', _external=True) + "topics/automation/automation-tools/task-automation/stata-error-handling-make/", code=301)

    @app.route('/topics/store-and-document-your-data/document-data/documenting-new-data/')
    def redirect_87():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/share-your-work/content-creation/documenting-new-data/", code=301)

    @app.route('/building-blocks/collect-data/webscraping-apis/scrape-static-websites/')
    def redirect_88():
        return redirect(url_for('home', _external=True) + "topics/collect-store/data-collection/web-scraping/scrape-static-websites/", code=301)

    @app.route('/building-blocks/configure-your-computer/automation-and-workflows/teamviewer/')
    def redirect_89():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/project-management/project-management-gh/teamviewer/", code=301)

    @app.route('/tutorials/more-tutorials/write-your-first-latex-document/setup-latex/')
    def redirect_90():
        return redirect(url_for('home', _external=True) + "topics/research-skills/templates-dynamic-content/templates/write-your-first-latex-document/setup-latex/", code=301)

    @app.route('/building-blocks/store-and-document-your-data/document-data/documenting-new-data/')
    def redirect_91():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/share-your-work/content-creation/documenting-new-data/", code=301)

    @app.route('/building-blocks/analyze-data/machine-learning/introduction-to-machine-learning/')
    def redirect_92():
        return redirect(url_for('home', _external=True) + "topics/analyze/machine-learning/ml-intro/introduction-to-machine-learning/", code=301)

    @app.route('/building-blocks/collaborate-and-share-your-work/use-github/most-important-git-commands/')
    def redirect_93():
        return redirect(url_for('home', _external=True) + "topics/automation/version-control/start-git/most-important-git-commands/", code=301)

    @app.route('/tutorials/reproducible-research-and-automation/practicing-pipeline-automation-make/pipeline-automation-overview/')
    def redirect_94():
        return redirect(url_for('home', _external=True) + "topics/automation/automation-tools/makefiles/practicing-pipeline-automation-make/pipeline-automation-overview/", code=301)

    @app.route('/building-blocks/prepare-your-data-for-analysis/data-visualization/matplotlib-seaborn/')
    def redirect_95():
        return redirect(url_for('home', _external=True) + "topics/visualization/data-visualization/graphs-charts/matplotlib-seaborn/", code=301)

    @app.route('/tutorials/code-like-a-pro/hugo-website/hugo-website-overview/')
    def redirect_96():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/share-your-work/content-creation/hugo-website/hugo-website-overview/", code=301)

    @app.route('/building-blocks/collaborate-and-share-your-work/use-github/releases/')
    def redirect_97():
        return redirect(url_for('home', _external=True) + "topics/automation/version-control/repository-lifecycle/releases/", code=301)

    @app.route('/tutorials/more-tutorials/airbnb-workflow/conclusion/')
    def redirect_98():
        return redirect(url_for('home', _external=True) + "topics/automation/automation-tools/makefiles/airbnb-workflow/conclusion/", code=301)

    @app.route('/topics/automation/topics/collaborate-and-share-your-work/use-github/versioning-using-git')
    def redirect_99():
        return redirect(url_for('home', _external=True) + "topics/automation/version-control/start-git/versioning-using-git/", code=301)

    @app.route('/tutorials/scale-up/running-computations-remotely/')
    def redirect_100():
        return redirect(url_for('home', _external=True) + "topics/automation/replicability/cloud-computing/running-computations-remotely/", code=301)

    @app.route('/tutorials/scale-up/running-computations-remotely/terminate-instances/')
    def redirect_101():
        return redirect(url_for('home', _external=True) + "topics/automation/replicability/cloud-computing/running-computations-remotely/terminate-instances/", code=301)

    @app.route('/building-blocks/analyze-data/regressions/iv/')
    def redirect_102():
        return redirect(url_for('home', _external=True) + "topics/analyze/causal-inference/instrumental-variables/iv/", code=301)

    @app.route('/building-blocks/collect-data/workflows-for-online-data-collection/calculate-sample-size/')
    def redirect_103():
        return redirect(url_for('home', _external=True) + "topics/collect-store/data-collection/web-scraping/calculate-sample-size/", code=301)

    @app.route('/building-blocks/analyze-data/regression-discontinuity/validation-falsification/')
    def redirect_104():
        return redirect(url_for('home', _external=True) + "topics/analyze/causal-inference/rdd/validation-falsification/", code=301)

    @app.route('/building-blocks/collaborate-and-share-your-work/use-github/git-commits/')
    def redirect_105():
        return redirect(url_for('home', _external=True) + "topics/automation/version-control/advanced-git/git-commits/", code=301)

    @app.route('/building-blocks/store-and-document-your-data/store-data/choose-a-data-repository/')
    def redirect_106():
        return redirect(url_for('home', _external=True) + "topics/collect-store/data-storage/long-term-archiving/choose-a-data-repository/", code=301)

    @app.route('/building-blocks/collaborate-and-share-your-work/write-your-paper/latex-thesis-template.pdf')
    def redirect_107():
        return redirect(url_for('home', _external=True) + "topics/research-skills/templates-dynamic-content/templates/latex-thesis-template.pdf", code=301)

    @app.route('/building-blocks/configure-your-computer/automation-and-workflows/environment/')
    def redirect_108():
        return redirect(url_for('home', _external=True) + "topics/computer-setup/develop-coding-skills/bash/environment/", code=301)

    @app.route('/tutorials/more-tutorials/contribute-to-tilburg-science-hub/contribute/')
    def redirect_109():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/project-management/contribute-to-tilburg-science-hub/contribute/", code=301)

    @app.route('/tutorials/more-tutorials/contribute-to-tilburg-science-hub/tutorial-shell/')
    def redirect_110():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/project-management/contribute-to-tilburg-science-hub/tutorial-shell/", code=301)

    @app.route('/topics/contribute-and-share-your-work/most-important-git-commands/')
    def redirect_111():
        return redirect(url_for('home', _external=True) + "topics/automation/version-control/start-git/most-important-git-commands/", code=301)

    @app.route('/building-blocks/collect-data/webscraping-apis/extract-data-api/')
    def redirect_112():
        return redirect(url_for('home', _external=True) + "topics/collect-store/data-collection/apis/extract-data-api/", code=301)

    @app.route('/topics/configure-your-computer/automation-and-workflows/docker/')
    def redirect_113():
        return redirect(url_for('home', _external=True) + "topics/automation/replicability/docker/", code=301)

    @app.route('/tutorials/other-category/implement-an-efficient-and-reproducible-workflow/finish/')
    def redirect_114():
        return redirect(url_for('home', _external=True) + "topics/automation/automation-tools/makefiles/practicing-pipeline-automation-make/finish/", code=301)

    @app.route('/topics/collect-data/webscraping-apis/scrape-static-websites/')
    def redirect_115():
        return redirect(url_for('home', _external=True) + "topics/collect-store/data-collection/web-scraping/scrape-static-websites/", code=301)

    @app.route('/building-blocks/prepare-your-data-for-analysis/data-preparation/dask-in-action/')
    def redirect_116():
        return redirect(url_for('home', _external=True) + "topics/manage-manipulate/loading/large-datasets/dask-in-action/", code=301)

    @app.route('/topics/prepare-your-data-for-analysis/data-preparation/large-datasets-python/')
    def redirect_117():
        return redirect(url_for('home', _external=True) + "topics/manage-manipulate/loading/large-datasets/large-datasets-python/", code=301)

    @app.route('/building-blocks/store-and-document-your-data/store-data/environment-variables/')
    def redirect_118():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/project-management/project-management-gh/environment-variables/", code=301)

    @app.route('/building-blocks/automate-and-execute-your-work/reproducible-work/docker/')
    def redirect_119():
        return redirect(url_for('home', _external=True) + "topics/automation/replicability/docker/", code=301)

    @app.route('/topics/configure-your-computer/statistics-and-computation/python-packages/')
    def redirect_120():
        return redirect(url_for('home', _external=True) + "topics/computer-setup/software-installation/python/python-packages/", code=301)

    @app.route('/tutorials/more-tutorials/write-your-first-latex-document/what-is-latex/')
    def redirect_121():
        return redirect(url_for('home', _external=True) + "topics/research-skills/templates-dynamic-content/templates/write-your-first-latex-document/what-is-latex/", code=301)

    @app.route('/topics/analyze-data/regressions/impact-evaluation/')
    def redirect_122():
        return redirect(url_for('home', _external=True) + "topics/analyze/causal-inference/did/impact-evaluation/", code=301)

    @app.route('/topics/collaborate-and-share-your-work/use-github/naming-git-branches/')
    def redirect_123():
        return redirect(url_for('home', _external=True) + "topics/automation/version-control/advanced-git/naming-git-branches/", code=301)

    @app.route('/topics/configure-your-computer/statistics-and-computation/stata/')
    def redirect_124():
        return redirect(url_for('home', _external=True) + "topics/computer-setup/software-installation/stata/stata/", code=301)

    @app.route('/building-blocks/configure-your-computer/statistics-and-computation/sublime/')
    def redirect_125():
        return redirect(url_for('home', _external=True) + "topics/computer-setup/software-installation/document-creation/sublime/", code=301)

    @app.route('/building-blocks/develop-your-research-skills/tips/principles-good-coding/')
    def redirect_126():
        return redirect(url_for('home', _external=True) + "topics/computer-setup/develop-coding-skills/coding-practices/principles-good-coding/", code=301)

    @app.route('/tutorials/more-tutorials/implement-an-efficient-and-reproducible-workflow/wipe-rerun/')
    def redirect_127():
        return redirect(url_for('home', _external=True) + "topics/automation/automation-tools/makefiles/practicing-pipeline-automation-make/wipe-rerun/", code=301)

    @app.route('/tutorials/educational-support/hugo-website/go-live/')
    def redirect_128():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/share-your-work/content-creation/hugo-website/go-live/", code=301)

    @app.route('/tutorials/open-education/hugo-website/go-live')
    def redirect_129():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/share-your-work/content-creation/hugo-website/go-live/", code=301)

    @app.route('/tutorials/open-education/educational-videos/educational-videos-overview/')
    def redirect_130():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/share-your-work/content-creation/educational-videos/educational-videos-overview/", code=301)

    @app.route('/tutorials/open-education/hugo-website/go-live/')
    def redirect_131():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/share-your-work/content-creation/hugo-website/go-live/", code=301)

    @app.route('/tutorials/reproducible-research-and-automation/principles-of-project-setup-and-workflow-management/structure_spotify_2018')
    def redirect_132():
        return redirect(url_for('home', _external=True) + "topics/automation/workflows/starting/principles-of-project-setup-and-workflow-management/structure_spotify_2018", code=301)

    @app.route('/topics/automation/version-control/start-git/git-ignore')
    def redirect_133():
        return redirect(url_for('home', _external=True) + "topics/automation/version-control/advanced-git/git-ignore/", code=301)

    @app.route('/topics/collect-data/webscraping-apis/scrape-dynamic-websites/')
    def redirect_134():
        return redirect(url_for('home', _external=True) + "topics/collect-store/data-collection/web-scraping/scrape-dynamic-websites/", code=301)

    @app.route('/building-blocks/analyze-data/regression-discontinuity/fuzzy-example/')
    def redirect_135():
        return redirect(url_for('home', _external=True) + "topics/analyze/causal-inference/rdd/fuzzy-example/", code=301)

    @app.route('/building-blocks/develop-your-research-skills/tips/texteditors/')
    def redirect_136():
        return redirect(url_for('home', _external=True) + "topics/computer-setup/software-installation/ide/texteditors/", code=301)

    @app.route('/building-blocks/collaborate-and-share-your-work/write-your-paper/amsmath-latex-cheatsheet/')
    def redirect_137():
        return redirect(url_for('home', _external=True) + "topics/research-skills/templates-dynamic-content/templates/amsmath-latex-cheatsheet/", code=301)

    @app.route('/building-blocks/automate-and-execute-your-work/reproducible-work/monitor-memory-vm/')
    def redirect_138():
        return redirect(url_for('home', _external=True) + "topics/automation/replicability/cloud-computing/monitor-memory-vm/", code=301)

    @app.route('/topics/configure-your-computer/statistics-and-computation/r/')
    def redirect_139():
        return redirect(url_for('home', _external=True) + "topics/computer-setup/software-installation/rstudio/r/", code=301)

    @app.route('/tutorials/more-tutorials/running-computations-remotely/run-scripts/')
    def redirect_140():
        return redirect(url_for('home', _external=True) + "topics/automation/replicability/cloud-computing/running-computations-remotely/run-scripts/", code=301)

    @app.route('/tutorials/scale-up/running-computations-remotely/run-scripts')
    def redirect_141():
        return redirect(url_for('home', _external=True) + "topics/automation/replicability/cloud-computing/running-computations-remotely/run-scripts/", code=301)

    @app.route('/building-blocks/configure-your-computer/statistics-and-computation/latex/')
    def redirect_142():
        return redirect(url_for('home', _external=True) + "topics/computer-setup/software-installation/document-creation/latex/", code=301)

    @app.route('/building-blocks/collect-data/workflows-for-online-data-collection/data-availability-assessment/')
    def redirect_143():
        return redirect(url_for('home', _external=True) + "topics/collect-store/data-collection/web-scraping/data-availability-assessment/", code=301)

    @app.route('/building-blocks/analyze-data/regressions-paneldata/between_estimator/')
    def redirect_144():
        return redirect(url_for('home', _external=True) + "topics/analyze/causal-inference/panel-data/between_estimator/", code=301)

    @app.route('/building-blocks/configure-your-computer/statistics-and-computation/r/')
    def redirect_145():
        return redirect(url_for('home', _external=True) + "topics/computer-setup/software-installation/rstudio/r/", code=301)

    @app.route('/building-blocks/configure-your-computer/infrastructure-choice/cartesius_cluster/')
    def redirect_146():
        return redirect(url_for('home', _external=True) + "topics/automation/replicability/cloud-computing/cartesius_cluster/", code=301)

    @app.route('/topics/automate-and-execute-your-work/automate-your-workflow/intro_ghactions/')
    def redirect_147():
        return redirect(url_for('home', _external=True) + "topics/automation/automation-tools/deployment/intro_ghactions/", code=301)

    @app.route('/tutorials/code-like-a-pro/web-scraping/')
    def redirect_148():
        return redirect(url_for('home', _external=True) + "topics/collect-store/data-collection/web-scraping/", code=301)

    @app.route('/topics/more-tutorials/contribute-to-tilburg-science-hub/contribute/')
    def redirect_149():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/project-management/contribute-to-tilburg-science-hub/contribute/", code=301)

    @app.route('/topics/collaborate-and-share-your-work/use-github/git-branching-strategies/')
    def redirect_150():
        return redirect(url_for('home', _external=True) + "topics/automation/version-control/advanced-git/git-branching-strategies/", code=301)

    @app.route('/topics/configure-your-computer/statistics-and-computation/git/')
    def redirect_151():
        return redirect(url_for('home', _external=True) + "topics/automation/version-control/start-git/git/", code=301)

    @app.route('/topics/analyze-data/regressions/regression-analysis/')
    def redirect_152():
        return redirect(url_for('home', _external=True) + "topics/analyze/regression/linear-regression/regression-analysis/", code=301)

    @app.route('/topics/configure-your-computer/automation-and-workflows/commandline/')
    def redirect_153():
        return redirect(url_for('home', _external=True) + "topics/computer-setup/develop-coding-skills/bash/commandline/", code=301)

    @app.route('/building-blocks/automate-and-execute-your-work/automate-your-workflow/task-scheduling/')
    def redirect_154():
        return redirect(url_for('home', _external=True) + "topics/automation/automation-tools/task-automation/task-scheduling/", code=301)

    @app.route('/building-blocks/configure-your-computer/statistics-and-computation/vscode/')
    def redirect_155():
        return redirect(url_for('home', _external=True) + "topics/computer-setup/software-installation/ide/vscode/", code=301)

    @app.route('/topics/configure-your-computer/statistics-and-computation/latex/')
    def redirect_156():
        return redirect(url_for('home', _external=True) + "topics/computer-setup/software-installation/document-creation/latex/", code=301)

    @app.route('/building-blocks/collaborate-and-share-your-work/use-github/mothball/')
    def redirect_157():
        return redirect(url_for('home', _external=True) + "topics/automation/version-control/repository-lifecycle/mothball/", code=301)

    @app.route('/topics/configure-your-computer/infrastructure-choice/getting-started-research-cloud/')
    def redirect_158():
        return redirect(url_for('home', _external=True) + "topics/automation/replicability/cloud-computing/getting-started-research-cloud/", code=301)

    @app.route('/topics/configure-your-computer/infrastructure-choice/hpc_tiu/')
    def redirect_159():
        return redirect(url_for('home', _external=True) + "topics/automation/replicability/cloud-computing/hpc_tiu/", code=301)

    @app.route('/topics/project-setup/principles-of-project-setup-and-workflow-management/automation/')
    def redirect_160():
        return redirect(url_for('home', _external=True) + "topics/automation/workflows/starting/principles-of-project-setup-and-workflow-management/automation/", code=301)

    @app.route('/topics/share-your-results-and-project/use-github/versioning-using-git/')
    def redirect_161():
        return redirect(url_for('home', _external=True) + "topics/automation/version-control/start-git/versioning-using-git/", code=301)

    @app.route('/topics/automate-and-execute-your-work/reproducible-work/dockerhub/')
    def redirect_162():
        return redirect(url_for('home', _external=True) + "topics/automation/replicability/docker/dockerhub/", code=301)

    @app.route('/topics/automate-and-execute-your-work/reproducible-work/renv/')
    def redirect_163():
        return redirect(url_for('home', _external=True) + "topics/automation/replicability/package-management/renv/", code=301)

    @app.route('/building-blocks/configure-your-computer/infrastructure-choice/surf-research-drive/')
    def redirect_164():
        return redirect(url_for('home', _external=True) + "topics/collect-store/data-storage/surf-research-cloud/surf-research-drive/", code=301)

    @app.route('/topics/reproducible-research-and-automation/practicing-pipeline-automation-make/pipeline-automation-overview/')
    def redirect_165():
        return redirect(url_for('home', _external=True) + "topics/automation/automation-tools/makefiles/practicing-pipeline-automation-make/pipeline-automation-overview/", code=301)

    @app.route('/building-blocks/configure-your-computer/infrastructure-choice/hpc_tiu/')
    def redirect_166():
        return redirect(url_for('home', _external=True) + "topics/automation/replicability/cloud-computing/hpc_tiu/", code=301)

    @app.route('/building-blocks/collaborate-and-share-your-work/use-github/git-tools/')
    def redirect_167():
        return redirect(url_for('home', _external=True) + "topics/automation/version-control/advanced-git/git-tools/", code=301)

    @app.route('/building-blocks/configure-your-computer/automation-and-workflows/make/')
    def redirect_168():
        return redirect(url_for('home', _external=True) + "topics/automation/automation-tools/makefiles/make/", code=301)

    @app.route('/building-blocks/develop-your-research-skills/learn-to-code/learn-open-interpreter/')
    def redirect_169():
        return redirect(url_for('home', _external=True) + "topics/computer-setup/develop-coding-skills/bash/learn-open-interpreter/", code=301)

    @app.route('/building-blocks/collaborate-and-share-your-work/use-github/versioning-using-git')
    def redirect_170():
        return redirect(url_for('home', _external=True) + "topics/automation/version-control/start-git/versioning-using-git/", code=301)

    @app.route('/building-blocks/configure-your-computer/task-specific-configurations/virtual-environments/')
    def redirect_171():
        return redirect(url_for('home', _external=True) + "topics/computer-setup/software-installation/python/virtual-environments/", code=301)

    @app.route('/topics/develop-your-research-skills/tips/search-literature/')
    def redirect_172():
        return redirect(url_for('home', _external=True) + "topics/research-skills/writing/literature-review/search-literature/", code=301)

    @app.route('/building-blocks/automate-and-execute-your-work/reproducible-work/config-vm-gcp/')
    def redirect_173():
        return redirect(url_for('home', _external=True) + "topics/automation/replicability/cloud-computing/config-vm-gcp/", code=301)

    @app.route('/topics/automate-and-execute-your-work/reproducible-work/rstudio-aws/')
    def redirect_174():
        return redirect(url_for('home', _external=True) + "topics/automation/replicability/cloud-computing/rstudio-aws/", code=301)

    @app.route('/building-blocks/analyze-data/regressions-paneldata/within-estimator/')
    def redirect_175():
        return redirect(url_for('home', _external=True) + "topics/analyze/causal-inference/panel-data/within-estimator/", code=301)

    @app.route('/topics/reproducible-research-and-automation/principles-of-project-setup-and-workflow-management/directories/')
    def redirect_176():
        return redirect(url_for('home', _external=True) + "topics/automation/workflows/starting/principles-of-project-setup-and-workflow-management/directories/", code=301)

    @app.route('/building-blocks/automate-and-execute-your-work/automate-your-workflow/auto-install-r-packages/')
    def redirect_177():
        return redirect(url_for('home', _external=True) + "topics/automation/replicability/package-management/auto-install-r-packages/", code=301)

    @app.route('/topics/configure-your-computer/automation-and-workflows/make/')
    def redirect_178():
        return redirect(url_for('home', _external=True) + "topics/automation/automation-tools/makefiles/make/", code=301)

    @app.route('/building-blocks/analyze-data/regressions-paneldata/paneldata/')
    def redirect_179():
        return redirect(url_for('home', _external=True) + "topics/analyze/causal-inference/panel-data/paneldata/", code=301)

    @app.route('/topics/automate-and-execute-your-work/automate-your-workflow/task-scheduling/')
    def redirect_180():
        return redirect(url_for('home', _external=True) + "topics/automation/automation-tools/task-automation/task-scheduling/", code=301)

    @app.route('/topics/analyze-data/regressions/model-assumptions/')
    def redirect_181():
        return redirect(url_for('home', _external=True) + "topics/analyze/regression/reporting/model-assumptions/", code=301)

    @app.route('/building-blocks/analyze-data/causal-inference/')
    def redirect_182():
        return redirect(url_for('home', _external=True) + "topics/analyze/causal-inference/", code=301)

    @app.route('/topics/automate-and-execute-your-work/reproducible-work/packrat/')
    def redirect_183():
        return redirect(url_for('home', _external=True) + "topics/automation/replicability/package-management/packrat/", code=301)

    @app.route('/topics/analyze-data/regressions/model-summary/')
    def redirect_184():
        return redirect(url_for('home', _external=True) + "topics/visualization/data-visualization/regression-results/model-summary/", code=301)

    @app.route('/tutorials/project-management/principles-of-project-setup-and-workflow-management/checklist/')
    def redirect_185():
        return redirect(url_for('home', _external=True) + "topics/automation/workflows/starting/principles-of-project-setup-and-workflow-management/checklist/", code=301)

    @app.route('/building-blocks/analyze-data/regression-discontinuity/synth-control/')
    def redirect_186():
        return redirect(url_for('home', _external=True) + "topics/analyze/causal-inference/did/synth-control/", code=301)

    @app.route('/topics/analyze-data/regressions/marginal-effect-r/')
    def redirect_187():
        return redirect(url_for('home', _external=True) + "topics/analyze/regression/linear-regression/marginal-effect-r/", code=301)

    @app.route('/topics/configure-your-computer/task-specific-configurations/configuring-python-for-webscraping/')
    def redirect_188():
        return redirect(url_for('home', _external=True) + "topics/computer-setup/software-installation/python/configuring-python-for-webscraping/", code=301)

    @app.route('/building-blocks/automate-and-execute-your-work/reproducible-work/rstudio-aws/')
    def redirect_189():
        return redirect(url_for('home', _external=True) + "topics/automation/replicability/cloud-computing/rstudio-aws/", code=301)

    @app.route('/building-blocks/analyze-data/regressions/estimatr/')
    def redirect_190():
        return redirect(url_for('home', _external=True) + "topics/analyze/regression/linear-regression/estimatr/", code=301)

    @app.route('/building-blocks/automate-and-execute-your-work/automate-your-workflow/fileexchanges/')
    def redirect_191():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/project-management/project-management-gh/fileexchanges/", code=301)

    @app.route('/topics/collaborate-and-share-your-work/project_management/write-good-issues/')
    def redirect_192():
        return redirect(url_for('home', _external=True) + "topics/automation/version-control/start-git/write-good-issues/", code=301)

    @app.route('/building-blocks/configure-your-computer/automation-and-workflows/docker/')
    def redirect_193():
        return redirect(url_for('home', _external=True) + "topics/automation/replicability/docker/", code=301)

    @app.route('/topics/automate-and-execute-your-work/reproducible-work/config-vm-gcp/')
    def redirect_194():
        return redirect(url_for('home', _external=True) + "topics/automation/replicability/cloud-computing/config-vm-gcp/", code=301)

    @app.route('/building-blocks/analyze-data/regressions-paneldata/pooled-ols/')
    def redirect_195():
        return redirect(url_for('home', _external=True) + "topics/analyze/causal-inference/panel-data/pooled-ols/", code=301)

    @app.route('/building-blocks/collaborate-and-share-your-work/project_management/git-project-board/')
    def redirect_196():
        return redirect(url_for('home', _external=True) + "topics/automation/version-control/start-git/git-project-board/", code=301)

    @app.route('/building-blocks/prepare-your-data-for-analysis/data-preparation/large-datasets-python/')
    def redirect_197():
        return redirect(url_for('home', _external=True) + "topics/manage-manipulate/loading/large-datasets/large-datasets-python/", code=301)

    @app.route('/tutorial/analysis/')
    def redirect_198():
        return redirect(url_for('home', _external=True) + "topics/automation/automation-tools/makefiles/practicing-pipeline-automation-make/analysis/", code=301)

    @app.route('/building-blocks/collaborate-and-share-your-work/project_management/write-good-issues/')
    def redirect_199():
        return redirect(url_for('home', _external=True) + "topics/automation/version-control/start-git/write-good-issues/", code=301)

    @app.route('/tutorials/more-tutorials/chatgpt-article/chat-gpt-research/')
    def redirect_200():
        return redirect(url_for('home', _external=True) + "topics/automation/ai/gpt-models/chat-gpt-research/", code=301)

    @app.route('/tutorials/reproducible-research-and-automation/share-data/share-data/')
    def redirect_201():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/project-management/project-management-gh/share-data/", code=301)

    @app.route('/building-blocks/analyze-data/regressions/synth-control/')
    def redirect_202():
        return redirect(url_for('home', _external=True) + "topics/analyze/causal-inference/did/synth-control/", code=301)

    @app.route('/building-blocks/configure-your-computer/statistics-and-computation/stata-packages/')
    def redirect_203():
        return redirect(url_for('home', _external=True) + "topics/computer-setup/software-installation/stata/stata-packages/", code=301)

    @app.route('/building-blocks/store-and-document-your-data/store-data/aws-s3-buckets/')
    def redirect_204():
        return redirect(url_for('home', _external=True) + "topics/collect-store/data-storage/commercial-cloud/aws-s3-buckets/", code=301)

    @app.route('/building-blocks/develop-your-research-skills/tips/r-code-style/')
    def redirect_205():
        return redirect(url_for('home', _external=True) + "topics/computer-setup/software-installation/rstudio/r-code-style/", code=301)

    @app.route('/building-blocks/store-and-document-your-data/store-data/download-data/')
    def redirect_206():
        return redirect(url_for('home', _external=True) + "topics/collect-store/data-storage/commercial-cloud/download-data/", code=301)

    @app.route('/building-blocks/develop-your-research-skills/learn-to-code/learn-regular-expressions/')
    def redirect_207():
        return redirect(url_for('home', _external=True) + "topics/manage-manipulate/manipulate-clean/textual/learn-regular-expressions/", code=301)

    @app.route('/building-blocks/configure-your-computer/statistics-and-computation/matlab/')
    def redirect_208():
        return redirect(url_for('home', _external=True) + "topics/computer-setup/software-installation/matlab/matlab/", code=301)

    @app.route('/building-blocks/configure-your-computer/infrastructure-choice/getting-started-research-cloud/')
    def redirect_209():
        return redirect(url_for('home', _external=True) + "topics/automation/replicability/cloud-computing/getting-started-research-cloud/", code=301)

    @app.route('/building-blocks/configure-your-computer/infrastructure-choice/google-colab/')
    def redirect_210():
        return redirect(url_for('home', _external=True) + "topics/automation/replicability/cloud-computing/google-colab/", code=301)

    @app.route('/building-blocks/analyze-data/regressions-paneldata/fixed-effects-assumptions/')
    def redirect_211():
        return redirect(url_for('home', _external=True) + "topics/analyze/regression/linear-regression/fixed-effects-assumptions/", code=301)

    @app.route('/building-blocks/collaborate-and-share-your-work/use-github/git-ignore/')
    def redirect_212():
        return redirect(url_for('home', _external=True) + "topics/automation/version-control/advanced-git/git-ignore/", code=301)

    @app.route('/building-blocks/collaborate-and-share-your-work/use-github/git-lfs/')
    def redirect_213():
        return redirect(url_for('home', _external=True) + "topics/automation/version-control/advanced-git/git-lfs/", code=301)

    @app.route('/building-blocks/automate-and-execute-your-work/reproducible-work/renv/')
    def redirect_214():
        return redirect(url_for('home', _external=True) + "topics/automation/replicability/package-management/renv/", code=301)

    @app.route('/building-blocks/analyze-data/regressions-paneldata/first-difference/')
    def redirect_215():
        return redirect(url_for('home', _external=True) + "topics/analyze/causal-inference/panel-data/first-difference/", code=301)

    @app.route('/building-blocks/collaborate-and-share-your-work/write-your-paper/overleaf/')
    def redirect_216():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/project-management/project-management-gh/overleaf/", code=301)

    @app.route('/building-blocks/analyze-data/regressions/kableextra/')
    def redirect_217():
        return redirect(url_for('home', _external=True) + "topics/visualization/reporting-tables/reportingtables/kableextra/", code=301)

    @app.route('/building-blocks/automate-and-execute-your-work/reproducible-work/packrat/')
    def redirect_218():
        return redirect(url_for('home', _external=True) + "topics/automation/replicability/package-management/packrat/", code=301)

    @app.route('/building-blocks/prepare-your-data-for-analysis/data-preparation/text-preprocessing/')
    def redirect_219():
        return redirect(url_for('home', _external=True) + "topics/manage-manipulate/manipulate-clean/textual/text-preprocessing/", code=301)

    @app.route('/tutorials/more-tutorials/openai-whisper/whisper/')
    def redirect_220():
        return redirect(url_for('home', _external=True) + "topics/automation/ai/transcription/whisper/", code=301)

    @app.route('/building-blocks/collaborate-and-share-your-work/publish-on-the-web/shiny-apps/')
    def redirect_221():
        return redirect(url_for('home', _external=True) + "topics/visualization/data-visualization/dashboarding/shiny-apps/", code=301)

    @app.route('/tutorials/more-tutorials/running-computations-remotely/terminate-instances/')
    def redirect_222():
        return redirect(url_for('home', _external=True) + "topics/automation/replicability/cloud-computing/running-computations-remotely/terminate-instances/", code=301)

    @app.route('/building-blocks/analyze-data/regressions-paneldata/random-effects/')
    def redirect_223():
        return redirect(url_for('home', _external=True) + "topics/analyze/causal-inference/panel-data/random-effects/", code=301)

    @app.route('/tutorials/more-tutorials/write-your-first-latex-document/your-first-article/')
    def redirect_224():
        return redirect(url_for('home', _external=True) + "topics/research-skills/templates-dynamic-content/templates/write-your-first-latex-document/your-first-article/", code=301)

    @app.route('/building-blocks/collect-data/webscraping-apis/scrape-dynamic-websites/')
    def redirect_225():
        return redirect(url_for('home', _external=True) + "topics/collect-store/data-collection/web-scraping/scrape-dynamic-websites/", code=301)

    @app.route('/tutorials/project-setup/principles-of-project-setup-and-workflow-management/')
    def redirect_226():
        return redirect(url_for('home', _external=True) + "topics/automation/workflows/starting/principles-of-project-setup-and-workflow-management/", code=301)

    @app.route('/tutorials/reproducible-research-and-automation/principles-of-project-setup-and-workflow-management/collaboration/')
    def redirect_227():
        return redirect(url_for('home', _external=True) + "topics/automation/workflows/starting/principles-of-project-setup-and-workflow-management/collaboration/", code=301)

    @app.route('/building-blocks/prepare-your-data-for-analysis/data-preparation/spss-files-in-r/')
    def redirect_228():
        return redirect(url_for('home', _external=True) + "topics/manage-manipulate/loading/getting-started/spss-files-in-r/", code=301)

    @app.route('/tutorials/reproducible-research/practicing-pipeline-automation-make/')
    def redirect_229():
        return redirect(url_for('home', _external=True) + "topics/automation/automation-tools/makefiles/practicing-pipeline-automation-make/", code=301)

    @app.route('/tutorials/project-management/principles-of-project-setup-and-workflow-management/')
    def redirect_230():
        return redirect(url_for('home', _external=True) + "topics/automation/workflows/starting/principles-of-project-setup-and-workflow-management/", code=301)

    @app.route('/tutorials/reproducible-research-and-automation/principles-of-project-setup-and-workflow-management/')
    def redirect_231():
        return redirect(url_for('home', _external=True) + "topics/automation/workflows/starting/principles-of-project-setup-and-workflow-management/", code=301)

    @app.route('/tutorials/more-tutorials/airbnb-workflow/automating_workflows/')
    def redirect_232():
        return redirect(url_for('home', _external=True) + "topics/automation/automation-tools/makefiles/airbnb-workflow/automating_workflows/", code=301)

    @app.route('/tutorials/code-like-a-pro/hugo-website/')
    def redirect_233():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/share-your-work/content-creation/hugo-website/", code=301)

    @app.route('/building-blocks/prepare-your-data-for-analysis/data-visualization/')
    def redirect_234():
        return redirect(url_for('home', _external=True) + "topics/visualization/data-visualization/", code=301)

    @app.route('/tutorials/more-tutorials/write-your-first-latex-document/latex-tips/')
    def redirect_235():
        return redirect(url_for('home', _external=True) + "topics/research-skills/templates-dynamic-content/templates/write-your-first-latex-document/latex-tips/", code=301)

    @app.route('/building-blocks/analyze-data/regressions/regression-analysis/')
    def redirect_236():
        return redirect(url_for('home', _external=True) + "topics/analyze/regression/linear-regression/regression-analysis/", code=301)

    @app.route('/building-blocks/store-and-document-your-data/document-data/readme-best-practices/')
    def redirect_237():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/share-your-work/content-creation/readme-best-practices/", code=301)

    @app.route('/building-blocks/analyze-data/regressions/deltamethod/')
    def redirect_238():
        return redirect(url_for('home', _external=True) + "topics/analyze/causal-inference/instrumental-variables/deltamethod/", code=301)

    @app.route('/building-blocks/collaborate-and-share-your-work/write-your-paper/bookdown-theses/')
    def redirect_239():
        return redirect(url_for('home', _external=True) + "topics/research-skills/templates-dynamic-content/templates/bookdown-theses/", code=301)

    @app.route('/building-blocks/automate-and-execute-your-work/reproducible-work/dockerhub/')
    def redirect_240():
        return redirect(url_for('home', _external=True) + "topics/automation/replicability/docker/dockerhub/", code=301)

    @app.route('/building-blocks/develop-your-research-skills/learn-to-code/learn-r/')
    def redirect_241():
        return redirect(url_for('home', _external=True) + "topics/computer-setup/software-installation/rstudio/learn-r/", code=301)

    @app.route('/building-blocks/analyze-data/regressions/model-summary/')
    def redirect_242():
        return redirect(url_for('home', _external=True) + "topics/visualization/data-visualization/regression-results/model-summary/", code=301)

    @app.route('/building-blocks/collect-data/workflows-for-online-data-collection/online-data-collection-management/')
    def redirect_243():
        return redirect(url_for('home', _external=True) + "topics/collect-store/data-collection/databases/online-data-collection-management/", code=301)

    @app.route('/tutorials/project-management/principles-of-project-setup-and-workflow-management/collaboration/')
    def redirect_244():
        return redirect(url_for('home', _external=True) + "topics/automation/workflows/starting/principles-of-project-setup-and-workflow-management/collaboration/", code=301)

    @app.route('/tutorials/reproducible-research/getting-started-with-r/getting-started-with-r-overview/')
    def redirect_245():
        return redirect(url_for('home', _external=True) + "topics/computer-setup/software-installation/rstudio/getting-started-with-r-overview/", code=301)

    @app.route('/building-blocks/configure-your-computer/statistics-and-computation/pandoc/')
    def redirect_246():
        return redirect(url_for('home', _external=True) + "topics/computer-setup/software-installation/document-creation/pandoc/", code=301)

    @app.route('/tutorials/code-like-a-pro/getting-started-with-r/getting-started-with-r-overview')
    def redirect_247():
        return redirect(url_for('home', _external=True) + "topics/computer-setup/software-installation/rstudio/getting-started-with-r-overview/", code=301)

    @app.route('/building-blocks/automate-and-execute-your-work/automate-your-workflow/workflow-checklist/')
    def redirect_248():
        return redirect(url_for('home', _external=True) + "topics/automation/workflows/auditing/workflow-checklist/", code=301)

    @app.route('/tutorials/more-tutorials/educational-videos/educational-videos-overview/')
    def redirect_249():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/share-your-work/content-creation/educational-videos/educational-videos-overview/", code=301)

    @app.route('/building-blocks/analyze-data/regression-discontinuity/sharp-rdd/')
    def redirect_250():
        return redirect(url_for('home', _external=True) + "topics/analyze/causal-inference/rdd/sharp-rdd/", code=301)

    @app.route('/tutorials/more-tutorials/running-computations-remotely/move-files/')
    def redirect_251():
        return redirect(url_for('home', _external=True) + "topics/automation/replicability/cloud-computing/running-computations-remotely/move-files/", code=301)

    @app.route('/topics/more-tutorials/contribute-to-tilburg-science-hub/pullrequests/')
    def redirect_252():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/project-management/contribute-to-tilburg-science-hub/pullrequests/", code=301)

    @app.route('/tutorials/more-tutorials/write-an-academic-paper/')
    def redirect_253():
        return redirect(url_for('home', _external=True) + "topics/research-skills/writing/writing-process/write-an-academic-paper/", code=301)

    @app.route('/tutorials/more-tutorials/educational-videos/equipment-edu-videos')
    def redirect_254():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/share-your-work/content-creation/educational-videos/equipment-edu-videos/", code=301)

    @app.route('/tutorials/more-tutorials/educational-videos/equipment-edu-videos/')
    def redirect_255():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/share-your-work/content-creation/educational-videos/equipment-edu-videos/", code=301)

    @app.route('/building-blocks/develop-your-research-skills/tips/reference-list/')
    def redirect_256():
        return redirect(url_for('home', _external=True) + "topics/research-skills/writing/citations/reference-list/", code=301)

    @app.route('/tutorials/reproducible-research-and-automation/principles-of-project-setup-and-workflow-management/versioning/')
    def redirect_257():
        return redirect(url_for('home', _external=True) + "topics/automation/workflows/starting/principles-of-project-setup-and-workflow-management/versioning/", code=301)

    @app.route('/tutorials/project-management/principles-of-project-setup-and-workflow-management/versioning')
    def redirect_258():
        return redirect(url_for('home', _external=True) + "topics/automation/workflows/starting/principles-of-project-setup-and-workflow-management/versioning/", code=301)

    @app.route('/tutorials/more-tutorials/contribute-to-tilburg-science-hub/contribute')
    def redirect_259():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/project-management/contribute-to-tilburg-science-hub/contribute/", code=301)

    @app.route('/building-blocks/configure-your-computer/statistics-and-computation/python-packages/')
    def redirect_260():
        return redirect(url_for('home', _external=True) + "topics/computer-setup/software-installation/python/python-packages/", code=301)

    @app.route('/tutorials/more-tutorials/contribute-to-tilburg-science-hub/contribute/')
    def redirect_261():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/project-management/contribute-to-tilburg-science-hub/contribute/", code=301)

    @app.route('/building-blocks/collaborate-and-share-your-work/use-github/pull-requests')
    def redirect_262():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/project-management/engage-open-science/pull-requests/", code=301)

    @app.route('/building-blocks/collect-data/workflows-for-online-data-collection/online-data-sources-for-economists/')
    def redirect_263():
        return redirect(url_for('home', _external=True) + "topics/collect-store/data-collection/databases/online-data-sources-for-economists/", code=301)

    @app.route('/building-blocks/collaborate-and-share-your-work/write-your-paper/stata-graphs/')
    def redirect_264():
        return redirect(url_for('home', _external=True) + "topics/visualization/data-visualization/graphs-charts/stata-graphs/", code=301)

    @app.route('/building-blocks/collaborate-and-share-your-work/use-github/pull-requests/')
    def redirect_265():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/project-management/engage-open-science/pull-requests/", code=301)

    @app.route('/building-blocks/automate-and-execute-your-work/automate-your-workflow/stata-error-handling-make/')
    def redirect_266():
        return redirect(url_for('home', _external=True) + "topics/automation/automation-tools/task-automation/stata-error-handling-make/", code=301)

    @app.route('/building-blocks/automate-and-execute-your-work/automate-your-workflow/autofilling-values/')
    def redirect_267():
        return redirect(url_for('home', _external=True) + "topics/visualization/reporting-tables/reportingtables/autofilling-values/", code=301)

    @app.route('/tutorials/more-tutorials/write-your-first-latex-document/bibliography/')
    def redirect_268():
        return redirect(url_for('home', _external=True) + "topics/research-skills/templates-dynamic-content/templates/write-your-first-latex-document/bibliography/", code=301)

    @app.route('/tutorials/reproducible-research-and-automation/principles-of-project-setup-and-workflow-management/automation/')
    def redirect_269():
        return redirect(url_for('home', _external=True) + "topics/automation/workflows/starting/principles-of-project-setup-and-workflow-management/automation/", code=301)

    @app.route('/tutorials/project-setup/principles-of-project-setup-and-workflow-management/structure_phd_2013')
    def redirect_270():
        return redirect(url_for('home', _external=True) + "topics/automation/workflows/starting/principles-of-project-setup-and-workflow-management/structure_phd_2013", code=301)

    @app.route('/tutorials/code-like-a-pro/getting-started-with-stata/')
    def redirect_271():
        return redirect(url_for('home', _external=True) + "topics/computer-setup/software-installation/stata/getting-started-with-stata/", code=301)

    @app.route('/tutorials/more-tutorials/contribute-to-tilburg-science-hub/add-contributor/')
    def redirect_272():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/project-management/engage-open-science/contribute-to-tilburg-science-hub/add-contributor/", code=301)

    @app.route('/tutorials/reproducible-research-and-automation/principles-of-project-setup-and-workflow-management/structure_phd_2013')
    def redirect_273():
        return redirect(url_for('home', _external=True) + "topics/automation/workflows/starting/principles-of-project-setup-and-workflow-management/structure_phd_2013", code=301)

    @app.route('/tutorials/more-tutorials/airbnb-workflow/exporting_data/')
    def redirect_274():
        return redirect(url_for('home', _external=True) + "topics/automation/automation-tools/makefiles/airbnb-workflow/exporting_data/", code=301)

    @app.route('/tutorials/more-tutorials/contribute-to-tilburg-science-hub/building-block-shell/')
    def redirect_275():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/project-management/contribute-to-tilburg-science-hub/building-block-shell/", code=301)

    @app.route('/building-blocks/automate-and-execute-your-work/reproducible-work/mem-storage-gcp/')
    def redirect_276():
        return redirect(url_for('home', _external=True) + "topics/collect-store/data-storage/commercial-cloud/mem-storage-gcp/", code=301)

    @app.route('/building-blocks/configure-your-computer/statistics-and-computation/texmacs/')
    def redirect_277():
        return redirect(url_for('home', _external=True) + "topics/computer-setup/software-installation/document-creation/texmacs/", code=301)

    @app.route('/building-blocks/automate-and-execute-your-work/reproducible-work/software-environments/')
    def redirect_278():
        return redirect(url_for('home', _external=True) + "topics/automation/replicability/docker/software-environments/", code=301)

    @app.route('/tutorials/building-blocks/collaborate-and-share-your-work/use-github/versioning-using-git/')
    def redirect_279():
        return redirect(url_for('home', _external=True) + "topics/automation/version-control/start-git/versioning-using-git/", code=301)

    @app.route('/tutorials/more-tutorials/running-computations-remotely/cloud-computing')
    def redirect_280():
        return redirect(url_for('home', _external=True) + "topics/automation/replicability/cloud-computing/running-computations-remotely/cloud-computing/", code=301)

    @app.route('/building-blocks/configure-your-computer/infrastructure-choice/infrastructure-requirements/')
    def redirect_281():
        return redirect(url_for('home', _external=True) + "topics/automation/workflows/starting/infrastructure-requirements/", code=301)

    @app.route('/tutorials/more-tutorials/write-an-academic-paper/write-an-academic-paper/')
    def redirect_282():
        return redirect(url_for('home', _external=True) + "topics/research-skills/writing/writing-process/write-an-academic-paper/", code=301)

    @app.route('/tutorials/project-management/principles-of-project-setup-and-workflow-management/collaboration')
    def redirect_283():
        return redirect(url_for('home', _external=True) + "topics/automation/workflows/starting/principles-of-project-setup-and-workflow-management/collaboration/", code=301)

    @app.route('/tutorials/reproducible-research/start-new-project/starting-up-a-new-project/')
    def redirect_284():
        return redirect(url_for('home', _external=True) + "topics/automation/workflows/starting/starting-up-a-new-project/", code=301)

    @app.route('/tutorials/more-tutorials/running-computations-remotely/launch-instance/')
    def redirect_285():
        return redirect(url_for('home', _external=True) + "topics/automation/replicability/cloud-computing/running-computations-remotely/launch-instance/", code=301)

    @app.route('/tutorials/code-like-a-pro/hugo-website/go-live')
    def redirect_286():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/share-your-work/content-creation/hugo-website/go-live/", code=301)

    @app.route('/tutorials/code-like-a-pro/github-copilot/github-copilot/')
    def redirect_287():
        return redirect(url_for('home', _external=True) + "topics/automation/ai/gpt-models/github-copilot/", code=301)

    @app.route('/tutorials/scale-up/running-computations-remotely/launch-instance/')
    def redirect_288():
        return redirect(url_for('home', _external=True) + "topics/automation/replicability/cloud-computing/running-computations-remotely/launch-instance/", code=301)

    @app.route('/tutorials/more-tutorials/airbnb-workflow/transforming_data/')
    def redirect_289():
        return redirect(url_for('home', _external=True) + "topics/automation/automation-tools/makefiles/airbnb-workflow/transforming_data/", code=301)

    @app.route('/tutorials/code-like-a-pro/hugo-website/go-live/')
    def redirect_290():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/share-your-work/content-creation/hugo-website/go-live/", code=301)

    @app.route('/tutorials/project-management/principles-of-project-setup-and-workflow-management/project-setup-overview')
    def redirect_291():
        return redirect(url_for('home', _external=True) + "topics/automation/workflows/starting/principles-of-project-setup-and-workflow-management/project-setup-overview/", code=301)

    @app.route('/building-blocks/configure-your-computer/automation-and-workflows/commandline/')
    def redirect_292():
        return redirect(url_for('home', _external=True) + "topics/computer-setup/develop-coding-skills/bash/commandline/", code=301)

    @app.route('/tutorials/project-management/principles-of-project-setup-and-workflow-management/directories')
    def redirect_293():
        return redirect(url_for('home', _external=True) + "topics/automation/workflows/starting/principles-of-project-setup-and-workflow-management/directories/", code=301)

    @app.route('/building-blocks/collect-data/workflows-for-online-data-collection/ensure-legal-compliance-web-scraping/')
    def redirect_294():
        return redirect(url_for('home', _external=True) + "topics/collect-store/data-collection/web-scraping/ensure-legal-compliance-web-scraping/", code=301)

    @app.route('/tutorials/reproducible-research/practicing-pipeline-automation-make/modifications/')
    def redirect_295():
        return redirect(url_for('home', _external=True) + "topics/automation/automation-tools/makefiles/practicing-pipeline-automation-make/modifications/", code=301)

    @app.route('/tutorials/reproducible-research-and-automation/principles-of-project-setup-and-workflow-management/directories')
    def redirect_296():
        return redirect(url_for('home', _external=True) + "topics/automation/workflows/starting/principles-of-project-setup-and-workflow-management/directories/", code=301)

    @app.route('/tutorials/project-management/principles-of-project-setup-and-workflow-management/directories/')
    def redirect_297():
        return redirect(url_for('home', _external=True) + "topics/automation/workflows/starting/principles-of-project-setup-and-workflow-management/directories/", code=301)

    @app.route('/building-blocks/develop-your-research-skills/tips/python-coding-style/')
    def redirect_298():
        return redirect(url_for('home', _external=True) + "topics/computer-setup/software-installation/python/python-coding-style/", code=301)

    @app.route('/tutorials/project-management/principles-of-project-setup-and-workflow-management/versioning/')
    def redirect_299():
        return redirect(url_for('home', _external=True) + "topics/automation/workflows/starting/principles-of-project-setup-and-workflow-management/versioning/", code=301)

    @app.route('/tutorials/project-management/principles-of-project-setup-and-workflow-management/project-setup-overview/')
    def redirect_300():
        return redirect(url_for('home', _external=True) + "topics/automation/workflows/starting/principles-of-project-setup-and-workflow-management/project-setup-overview/", code=301)

    @app.route('/topics/analyze-data/regressions/deltamethod/')
    def redirect_301():
        return redirect(url_for('home', _external=True) + "topics/analyze/causal-inference/instrumental-variables/deltamethod/", code=301)

    @app.route('/topics/configure-your-computer/infrastructure-choice/cartesius_cluster/')
    def redirect_302():
        return redirect(url_for('home', _external=True) + "topics/automation/replicability/cloud-computing/cartesius_cluster/", code=301)

    @app.route('/topics/configure-your-computer/infrastructure-choice/lisa_cluster/')
    def redirect_303():
        return redirect(url_for('home', _external=True) + "topics/automation/replicability/cloud-computing/lisa_cluster/", code=301)

    @app.route('/building-blocks/automate-and-execute-your-work/automate-your-workflow/ghactions-self-hosted-runner')
    def redirect_304():
        return redirect(url_for('home', _external=True) + "topics/automation/automation-tools/deployment/ghactions-self-hosted-runner/", code=301)

    @app.route('/building-blocks/collect-data/webscraping-apis/read-write-data-apis/')
    def redirect_305():
        return redirect(url_for('home', _external=True) + "topics/collect-store/data-collection/apis/read-write-data-apis/", code=301)

    @app.route('/topics/analyze-data/regression-discontinuity/fuzzy-rdd/')
    def redirect_306():
        return redirect(url_for('home', _external=True) + "topics/analyze/causal-inference/rdd/fuzzy-rdd/", code=301)

    @app.route('/topics/automate-and-execute-your-work/automate-your-workflow/ghactions-workflow/')
    def redirect_307():
        return redirect(url_for('home', _external=True) + "topics/automation/automation-tools/deployment/ghactions-workflow/", code=301)

    @app.route('/building-blocks/develop-your-research-skills/learn-to-code/learn-bash-commands/')
    def redirect_308():
        return redirect(url_for('home', _external=True) + "topics/computer-setup/develop-coding-skills/bash/learn-bash-commands/", code=301)

    @app.route('/tutorials/reproducible-research-and-automation/principles-of-project-setup-and-workflow-management/collaboration')
    def redirect_309():
        return redirect(url_for('home', _external=True) + "topics/automation/workflows/starting/principles-of-project-setup-and-workflow-management/collaboration/", code=301)

    @app.route('/tutorials/reproducible-research/practicing-pipeline-automation-make/pipeline-make/')
    def redirect_310():
        return redirect(url_for('home', _external=True) + "topics/automation/automation-tools/makefiles/practicing-pipeline-automation-make/pipeline-make/", code=301)

    @app.route('/building-blocks/develop-your-coding-skills/learn-to-code/learn-r/')
    def redirect_311():
        return redirect(url_for('home', _external=True) + "topics/computer-setup/software-installation/rstudio/learn-r/", code=301)

    @app.route('/tutorials/more-tutorials/contribute-to-tilburg-science-hub/style-guide')
    def redirect_312():
        return redirect(url_for('home', _external=True) + "topics/Collaborate-share/Project-management/contribute-to-tilburg-science-hub/style-guide/", code=301)

    @app.route('/tutorials/more-tutorials/running-computations-remotely/')
    def redirect_313():
        return redirect(url_for('home', _external=True) + "topics/automation/replicability/cloud-computing/running-computations-remotely/", code=301)

    @app.route('/topics/analyze-data/regressions/iv/')
    def redirect_314():
        return redirect(url_for('home', _external=True) + "topics/analyze/causal-inference/instrumental-variables/iv/", code=301)

    @app.route('/tutorials/building-blocks/collaborate-and-share-your-work/use-github/versioning-using-git')
    def redirect_315():
        return redirect(url_for('home', _external=True) + "topics/automation/version-control/start-git/versioning-using-git/", code=301)

    @app.route('/tutorials/scale-up/running-computations-remotely/cloud-computing')
    def redirect_316():
        return redirect(url_for('home', _external=True) + "topics/automation/replicability/cloud-computing/running-computations-remotely/cloud-computing/", code=301)

    @app.route('/tutorials/more-tutorials/write-an-academic-paper/write-an-academic-paper')
    def redirect_317():
        return redirect(url_for('home', _external=True) + "topics/research-skills/writing/writing-process/write-an-academic-paper/", code=301)

    @app.route('/tutorials/reproducible-research-and-automation/start-new-project/starting-up-a-new-project')
    def redirect_318():
        return redirect(url_for('home', _external=True) + "topics/automation/workflows/starting/starting-up-a-new-project/", code=301)

    @app.route('/tutorials/open-education/educational-videos/')
    def redirect_319():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/share-your-work/content-creation/educational-videos/", code=301)

    @app.route('/building-blocks/configure-your-computer/statistics-and-computation/python/')
    def redirect_320():
        return redirect(url_for('home', _external=True) + "topics/computer-setup/software-installation/python/", code=301)

    @app.route('/tutorials/reproducible-research-and-automation/principles-of-project-setup-and-workflow-management/project-setup-overview')
    def redirect_321():
        return redirect(url_for('home', _external=True) + "topics/automation/workflows/starting/principles-of-project-setup-and-workflow-management/project-setup-overview/", code=301)

    @app.route('/building-blocks/configure-your-computer/automation-and-workflows/snakemake/')
    def redirect_322():
        return redirect(url_for('home', _external=True) + "topics/automation/automation-tools/makefiles/snakemake/", code=301)

    @app.route('/tutorials/more-tutorials/educational-videos/educational-videos-overview')
    def redirect_323():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/share-your-work/content-creation/educational-videos/educational-videos-overview/", code=301)

    @app.route('/tutorials/project-management/principles-of-project-setup-and-workflow-management/automation/')
    def redirect_324():
        return redirect(url_for('home', _external=True) + "topics/automation/workflows/starting/principles-of-project-setup-and-workflow-management/automation/", code=301)

    @app.route('/tutorials/open-education/educational-videos/educational-videos-overview')
    def redirect_325():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/share-your-work/content-creation/educational-videos/educational-videos-overview/", code=301)

    @app.route('/topics/automate-and-execute-your-work/reproducible-work/mem-storage-gcp/')
    def redirect_326():
        return redirect(url_for('home', _external=True) + "topics/collect-store/data-storage/commercial-cloud/mem-storage-gcp/", code=301)

    @app.route('/topics/develop-your-research-skills/tips/reference-list/')
    def redirect_327():
        return redirect(url_for('home', _external=True) + "topics/research-skills/writing/citations/reference-list/", code=301)

    @app.route('/building-blocks/configure-your-computer/statistics-and-computation/stata/')
    def redirect_328():
        return redirect(url_for('home', _external=True) + "topics/computer-setup/software-installation/stata/stata/", code=301)

    @app.route('/topics/prepare-your-data-for-analysis/data-preparation/dask-in-action/')
    def redirect_329():
        return redirect(url_for('home', _external=True) + "topics/manage-manipulate/loading/large-datasets/dask-in-action/", code=301)

    @app.route('/topics/visualize-your-data/data-visualization/theory-best-practices/')
    def redirect_330():
        return redirect(url_for('home', _external=True) + "topics/visualization/data-visualization/graphs-charts/theory-best-practices/", code=301)

    @app.route('/tutorials/more-tutorials/running-computations-remotely/cloud-computing/')
    def redirect_331():
        return redirect(url_for('home', _external=True) + "topics/automation/replicability/cloud-computing/running-computations-remotely/cloud-computing/", code=301)

    @app.route('/tutorials/reproducible-research/start-new-project/starting-up-a-new-project')
    def redirect_332():
        return redirect(url_for('home', _external=True) + "topics/automation/workflows/starting/starting-up-a-new-project/", code=301)

    @app.route('/building-blocks/collaborate-and-share-your-work/use-github/mothball')
    def redirect_333():
        return redirect(url_for('home', _external=True) + "topics/automation/version-control/repository-lifecycle/mothball/", code=301)

    @app.route('/building-blocks/automate-and-execute-your-work/reproducible-work/mem-storage-gcp')
    def redirect_334():
        return redirect(url_for('home', _external=True) + "topics/collect-store/data-storage/commercial-cloud/mem-storage-gcp/", code=301)

    @app.route('/tutorials/project-management/principles-of-project-setup-and-workflow-management/documenting-data')
    def redirect_335():
        return redirect(url_for('home', _external=True) + "topics/automation/workflows/starting/principles-of-project-setup-and-workflow-management/documenting-data/", code=301)

    @app.route('/building-blocks/develop-your-research-skills/learn-to-code/learn-python-and-julia/')
    def redirect_336():
        return redirect(url_for('home', _external=True) + "topics/computer-setup/software-installation/python/learn-python-and-julia/", code=301)

    @app.route('/topics/code-like-a-pro/hugo-website/get-hugo/')
    def redirect_337():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/share-your-work/content-creation/hugo-website/get-hugo/", code=301)

    @app.route('/topics/develop-your-research-skills/tips/stata-code-style/')
    def redirect_338():
        return redirect(url_for('home', _external=True) + "topics/computer-setup/software-installation/stata/stata-code-style/", code=301)

    @app.route('/building-blocks/share-your-results-and-project/use-github/versioning-using-git/')
    def redirect_339():
        return redirect(url_for('home', _external=True) + "topics/automation/version-control/start-git/versioning-using-git/", code=301)

    @app.route('/tutorials/project-management/principles-of-project-setup-and-workflow-management/documenting-data/')
    def redirect_340():
        return redirect(url_for('home', _external=True) + "topics/automation/workflows/starting/principles-of-project-setup-and-workflow-management/documenting-data/", code=301)

    @app.route('/tutorials/reproducible-research/practicing-pipeline-automation-make/pipeline-automation-overview')
    def redirect_341():
        return redirect(url_for('home', _external=True) + "topics/automation/automation-tools/makefiles/practicing-pipeline-automation-make/pipeline-automation-overview/", code=301)

    @app.route('/topics/configure-your-computer/statistics-and-computation/python/')
    def redirect_342():
        return redirect(url_for('home', _external=True) + "topics/computer-setup/software-installation/python/", code=301)

    @app.route('/topics/code-like-a-pro/web-scraping/web-scraping-tutorial/')
    def redirect_343():
        return redirect(url_for('home', _external=True) + "topics/collect-store/data-collection/web-scraping/web-scraping-tutorial/", code=301)

    @app.route('/building-blocks/collaborate-and-share-your-work/use-github/releases')
    def redirect_344():
        return redirect(url_for('home', _external=True) + "topics/automation/version-control/repository-lifecycle/releases/", code=301)

    @app.route('/topics/develop-your-research-skills/tips/r-code-style/')
    def redirect_345():
        return redirect(url_for('home', _external=True) + "topics/computer-setup/software-installation/rstudio/r-code-style/", code=301)

    @app.route('/building-blocks/prepare-your-data-for-analysis/data-preparation/data-preparation-workflow-management/')
    def redirect_346():
        return redirect(url_for('home', _external=True) + "topics/manage-manipulate/loading/getting-started/data-preparation-workflow-management/", code=301)

    @app.route('/topics/automate-and-execute-your-work/reproducible-work/docker/')
    def redirect_347():
        return redirect(url_for('home', _external=True) + "topics/automation/replicability/docker/", code=301)

    @app.route('/tutorials/open-education/hugo-website/get-hugo/')
    def redirect_348():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/share-your-work/content-creation/hugo-website/get-hugo/", code=301)

    @app.route('/topics/develop-your-research-skills/tips/principles-good-coding/')
    def redirect_349():
        return redirect(url_for('home', _external=True) + "topics/computer-setup/develop-coding-skills/coding-practices/principles-good-coding/", code=301)

    @app.route('/tutorials/reproducible-research-and-automation/principles-of-project-setup-and-workflow-management/documenting-data')
    def redirect_350():
        return redirect(url_for('home', _external=True) + "topics/automation/workflows/starting/principles-of-project-setup-and-workflow-management/documenting-data/", code=301)

    @app.route('/tutorials/open-education/hugo-website/hugo-website-overview')
    def redirect_351():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/share-your-work/content-creation/hugo-website/hugo-website-overview/", code=301)

    @app.route('/tutorials/code-like-a-pro/hugo-website/hugo-website-overview')
    def redirect_352():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/share-your-work/content-creation/hugo-website/hugo-website-overview/", code=301)

    @app.route('/building-blocks/automate-and-execute-your-work/automate-your-workflow/intro_ghactions')
    def redirect_353():
        return redirect(url_for('home', _external=True) + "topics/automation/automation-tools/deployment/intro_ghactions/", code=301)

    @app.route('/tutorials/open-education/hugo-website/hugo-website-overview/')
    def redirect_354():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/share-your-work/content-creation/hugo-website/hugo-website-overview/", code=301)

    @app.route('/tutorials/reproducible-research-and-automation/practicing-pipeline-automation-make/finish/')
    def redirect_355():
        return redirect(url_for('home', _external=True) + "topics/automation/automation-tools/makefiles/practicing-pipeline-automation-make/finish/", code=301)

    @app.route('/tutorials/more-tutorials/airbnb-workflow/loading_data/')
    def redirect_356():
        return redirect(url_for('home', _external=True) + "topics/automation/automation-tools/makefiles/airbnb-workflow/loading_data/", code=301)

    @app.route('/building-blocks/analyze-data/regressions-paneldata/canonical-did-table/')
    def redirect_357():
        return redirect(url_for('home', _external=True) + "topics/analyze/causal-inference/did/canonical-did-table/", code=301)

    @app.route('/tutorials/scale-up/scrum-for-researchers/use-scrum-in-your-team')
    def redirect_358():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/project-management/big-team-science/use-scrum-in-your-team/", code=301)

    @app.route('/tutorials/scale-up/scrum-for-researchers/use-scrum-in-your-team/')
    def redirect_359():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/project-management/big-team-science/use-scrum-in-your-team/", code=301)

    @app.route('/tutorials/open-education/educational-videos/shooting-edu-videos')
    def redirect_360():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/share-your-work/content-creation/educational-videos/shooting-edu-videos/", code=301)

    @app.route('/building-blocks/configure-your-computer/statistics-and-computation/git')
    def redirect_361():
        return redirect(url_for('home', _external=True) + "topics/automation/version-control/start-git/git/", code=301)

    @app.route('/tutorials/open-education/educational-videos/shooting-edu-videos/')
    def redirect_362():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/share-your-work/content-creation/educational-videos/shooting-edu-videos/", code=301)

    @app.route('/building-blocks/configure-your-computer/statistics-and-computation/git/')
    def redirect_363():
        return redirect(url_for('home', _external=True) + "topics/automation/version-control/start-git/git/", code=301)

    @app.route('/building-blocks/collect-data/webscraping-apis/web-scraping/')
    def redirect_364():
        return redirect(url_for('home', _external=True) + "topics/collect-store/data-collection/web-scraping/", code=301)

    @app.route('/building-blocks/collaborate-and-share-your-work/use-github/github-workflow')
    def redirect_365():
        return redirect(url_for('home', _external=True) + "topics/automation/version-control/start-git/github-workflow/", code=301)

    @app.route('/building-blocks/develop-your-coding-skills/learn-to-code/learn-regular-expressions/')
    def redirect_366():
        return redirect(url_for('home', _external=True) + "topics/manage-manipulate/manipulate-clean/textual/learn-regular-expressions/", code=301)

    @app.route('/tutorials/reproducible-research-and-automation/principles-of-project-setup-and-workflow-management/versioning')
    def redirect_367():
        return redirect(url_for('home', _external=True) + "topics/automation/workflows/starting/principles-of-project-setup-and-workflow-management/versioning/", code=301)

    @app.route('/building-blocks/automate-and-execute-your-work/error-handling/stata-error-handling-make/')
    def redirect_368():
        return redirect(url_for('home', _external=True) + "topics/automation/automation-tools/task-automation/stata-error-handling-make/", code=301)

    @app.route('/tutorials/reproducible-research/practicing-pipeline-automation-make/pipeline-automation-overview/')
    def redirect_369():
        return redirect(url_for('home', _external=True) + "topics/automation/automation-tools/makefiles/practicing-pipeline-automation-make/pipeline-automation-overview/", code=301)

    @app.route('/building-blocks/store-and-document-your-data/store-data/choose-a-data-repository')
    def redirect_370():
        return redirect(url_for('home', _external=True) + "topics/collect-store/data-storage/long-term-archiving/choose-a-data-repository/", code=301)

    @app.route('/building-blocks/develop-your-research-skills/learn-to-code/learn-regular-expressions')
    def redirect_371():
        return redirect(url_for('home', _external=True) + "topics/manage-manipulate/manipulate-clean/textual/learn-regular-expressions/", code=301)

    @app.route('/building-blocks/configure-your-computer/automation-and-workflows/environment/')
    def redirect_372():
        return redirect(url_for('home', _external=True) + "topics/computer-setup/develop-coding-skills/bash/environment/", code=301)

    @app.route('/tutorials/more-tutorials/airbnb-workflow/airbnb-workflow-overview/')
    def redirect_373():
        return redirect(url_for('home', _external=True) + "topics/automation/automation-tools/makefiles/airbnb-workflow/airbnb-workflow-overview/", code=301)

    @app.route('/tutorial/analysis/')
    def redirect_374():
        return redirect(url_for('home', _external=True) + "topics/automation/automation-tools/makefiles/practicing-pipeline-automation-make/analysis/", code=301)

    @app.route('/building-blocks/configure-your-computer/statistics-and-computation/vscode')
    def redirect_375():
        return redirect(url_for('home', _external=True) + "topics/computer-setup/software-installation/ide/vscode/", code=301)

    @app.route('/tutorials/more-tutorials/educational-videos/shooting-edu-videos')
    def redirect_376():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/share-your-work/content-creation/educational-videos/shooting-edu-videos/", code=301)

    @app.route('/building-blocks/automate-and-execute-your-work/automate-your-workflow/ghactions-self-hosted-runner/')
    def redirect_377():
        return redirect(url_for('home', _external=True) + "topics/automation/automation-tools/deployment/ghactions-self-hosted-runner/", code=301)

    @app.route('/tutorials/code-like-a-pro/github-copilot/github-copilot')
    def redirect_378():
        return redirect(url_for('home', _external=True) + "topics/automation/ai/gpt-models/github-copilot/", code=301)

    @app.route('/building-blocks/automate-and-execute-your-work/reproducible-work/dockerhub')
    def redirect_379():
        return redirect(url_for('home', _external=True) + "topics/automation/replicability/docker/dockerhub/", code=301)

    @app.route('/tutorials/reproducible-research/share-data/share-data')
    def redirect_380():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/project-management/project-management-gh/share-data/", code=301)

    @app.route('/building-blocks/configure-your-computer/automation-and-workflows/teamviewer/')
    def redirect_381():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/project-management/project-management-gh/teamviewer/", code=301)

    @app.route('/building-blocks/configure-your-computer/statistics-and-computation/matlab/')
    def redirect_382():
        return redirect(url_for('home', _external=True) + "topics/computer-setup/software-installation/matlab/matlab/", code=301)

    @app.route('/building-blocks/collaborate-and-share-your-work/use-github/remove-files')
    def redirect_383():
        return redirect(url_for('home', _external=True) + "topics/automation/version-control/advanced-git/remove-files/", code=301)

    @app.route('/tutorials/more-tutorials/airbnb-workflow/airbnb-workflow-overview')
    def redirect_384():
        return redirect(url_for('home', _external=True) + "topics/automation/automation-tools/makefiles/airbnb-workflow/airbnb-workflow-overview/", code=301)

    @app.route('/tutorials/reproducible-research/share-data/share-data/')
    def redirect_385():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/project-management/project-management-gh/share-data/", code=301)

    @app.route('/building-blocks/automate-and-execute-your-work/reproducible-work/rstudio-aws')
    def redirect_386():
        return redirect(url_for('home', _external=True) + "topics/automation/replicability/cloud-computing/rstudio-aws/", code=301)

    @app.route('/building-blocks/configure-your-computer/automation-and-workflows/commandline/')
    def redirect_387():
        return redirect(url_for('home', _external=True) + "topics/computer-setup/develop-coding-skills/bash/commandline/", code=301)

    @app.route('/building-blocks/collaborate-and-share-your-work/use-github/git-lfs')
    def redirect_388():
        return redirect(url_for('home', _external=True) + "topics/automation/version-control/advanced-git/git-lfs/", code=301)

    @app.route('/building-blocks/configure-your-computer/statistics-and-computation/latex/')
    def redirect_389():
        return redirect(url_for('home', _external=True) + "topics/computer-setup/software-installation/document-creation/latex/", code=301)

    @app.route('/topics/develop-your-research-skills/tips/python-coding-style/')
    def redirect_390():
        return redirect(url_for('home', _external=True) + "topics/computer-setup/software-installation/python/python-coding-style/", code=301)

    @app.route('/building-blocks/configure-your-computer/automation-and-workflows/docker')
    def redirect_391():
        return redirect(url_for('home', _external=True) + "topics/automation/replicability/docker/", code=301)

    @app.route('/building-blocks/collaborate-and-share-your-work/project_management/write-good-issues')
    def redirect_392():
        return redirect(url_for('home', _external=True) + "topics/automation/version-control/start-git/write-good-issues/", code=301)

    @app.route('/tutorials/project-setup/principles-of-project-setup-and-workflow-management/collaboration/')
    def redirect_393():
        return redirect(url_for('home', _external=True) + "topics/automation/workflows/starting/principles-of-project-setup-and-workflow-management/collaboration/", code=301)

    @app.route('/tutorials/more-tutorials/write-your-first-latex-document/what-is-latex')
    def redirect_394():
        return redirect(url_for('home', _external=True) + "topics/research-skills/templates-dynamic-content/templates/write-your-first-latex-document/what-is-latex/", code=301)

    @app.route('/tutorials/reproducible-research-and-automation/practicing-pipeline-automation-make/pipeline-automation-overview')
    def redirect_395():
        return redirect(url_for('home', _external=True) + "topics/automation/automation-tools/makefiles/practicing-pipeline-automation-make/pipeline-automation-overview/", code=301)

    @app.route('/building-blocks/automate-and-execute-your-work/reproducible-work/docker')
    def redirect_396():
        return redirect(url_for('home', _external=True) + "topics/automation/replicability/docker/", code=301)

    @app.route('/building-blocks/collaborate-and-share-your-work/use-github/naming-git-branches')
    def redirect_397():
        return redirect(url_for('home', _external=True) + "topics/automation/version-control/advanced-git/naming-git-branches/", code=301)

    @app.route('/building-blocks/configure-your-computer/task-specific-configurations/configuring-python-for-webscraping/')
    def redirect_398():
        return redirect(url_for('home', _external=True) + "topics/computer-setup/software-installation/python/configuring-python-for-webscraping/", code=301)

    @app.route('/use/docker/')
    def redirect_399():
        return redirect(url_for('home', _external=True) + "topics/automation/replicability/docker/", code=301)

    @app.route('/building-blocks/collaborate-and-share-your-work/use-github/git-project-board/')
    def redirect_400():
        return redirect(url_for('home', _external=True) + "topics/automation/version-control/start-git/git-project-board/", code=301)

    @app.route('/tutorials/more-tutorials/web-scraping/web-scraping-tutorial')
    def redirect_401():
        return redirect(url_for('home', _external=True) + "topics/collect-store/data-collection/web-scraping/web-scraping-tutorial/", code=301)

    @app.route('/tutorials/more-tutorials/web-scraping/web-scraping-tutorial/')
    def redirect_402():
        return redirect(url_for('home', _external=True) + "topics/collect-store/data-collection/web-scraping/web-scraping-tutorial/", code=301)

    @app.route('/building-blocks/collaborate-and-share-your-work/project_management/git-project-board')
    def redirect_403():
        return redirect(url_for('home', _external=True) + "topics/automation/version-control/start-git/git-project-board/", code=301)

    @app.route('/tutorials/code-like-a-pro/web-scraping/web-scraping-tutorial')
    def redirect_404():
        return redirect(url_for('home', _external=True) + "topics/collect-store/data-collection/web-scraping/web-scraping-tutorial/", code=301)

    @app.route('/building-blocks/automate-and-execute-your-work/automate-your-workflow/software-environments/')
    def redirect_405():
        return redirect(url_for('home', _external=True) + "topics/automation/replicability/docker/software-environments/", code=301)

    @app.route('/tutorials/more-tutorials/chatgpt-article/chat-gpt-research')
    def redirect_406():
        return redirect(url_for('home', _external=True) + "topics/automation/ai/gpt-models/chat-gpt-research/", code=301)

    @app.route('/building-blocks/collaborate-and-share-your-work/use-github/make-code-citable-with-doi')
    def redirect_407():
        return redirect(url_for('home', _external=True) + "topics/automation/version-control/repository-lifecycle/make-code-citable-with-doi/", code=301)

    @app.route('/building-blocks/collaborate-and-share-your-work/use-github/git-ignore')
    def redirect_408():
        return redirect(url_for('home', _external=True) + "topics/automation/version-control/advanced-git/git-ignore/", code=301)

    @app.route('/tutorials/reproducible-research-and-automation/share-data/share-data')
    def redirect_409():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/project-management/project-management-gh/share-data/", code=301)

    @app.route('/building-blocks/configure-your-computer/statistics-and-computation/r/')
    def redirect_410():
        return redirect(url_for('home', _external=True) + "topics/computer-setup/software-installation/rstudio/r/", code=301)

    @app.route('/setup/make/')
    def redirect_411():
        return redirect(url_for('home', _external=True) + "topics/automation/automation-tools/makefiles/make/", code=301)

    @app.route('/building-blocks/configure-your-computer/statistics-and-computation/pandoc/')
    def redirect_412():
        return redirect(url_for('home', _external=True) + "topics/computer-setup/software-installation/document-creation/pandoc/", code=301)

    @app.route('/tutorials/reproducible-research-and-automation/principles-of-project-setup-and-workflow-management/automation')
    def redirect_413():
        return redirect(url_for('home', _external=True) + "topics/automation/workflows/starting/principles-of-project-setup-and-workflow-management/automation/", code=301)

    @app.route('/building-blocks/configure-your-computer/infrastructure-choice/fileexchanges/')
    def redirect_414():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/project-management/project-management-gh/fileexchanges/", code=301)

    @app.route('/tutorials/project-management/principles-of-project-setup-and-workflow-management/automation')
    def redirect_415():
        return redirect(url_for('home', _external=True) + "topics/automation/workflows/starting/principles-of-project-setup-and-workflow-management/automation/", code=301)

    @app.route('/tutorials/open-education/hugo-website/pick-theme/')
    def redirect_416():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/share-your-work/content-creation/hugo-website/pick-theme/", code=301)

    @app.route('/building-blocks/collaborate-and-share-your-work/use-github/git-branching-strategies')
    def redirect_417():
        return redirect(url_for('home', _external=True) + "topics/automation/version-control/advanced-git/git-branching-strategies/", code=301)

    @app.route('/building-blocks/configure-your-computer/automation-and-workflows/make')
    def redirect_418():
        return redirect(url_for('home', _external=True) + "topics/automation/automation-tools/makefiles/make/", code=301)

    @app.route('/building-blocks/collaborate-and-share-your-work/use-github/write-good-issues/')
    def redirect_419():
        return redirect(url_for('home', _external=True) + "topics/automation/version-control/start-git/write-good-issues/", code=301)

    @app.route('/building-blocks/configure-your-computer/statistics-and-computation/python-packages/')
    def redirect_420():
        return redirect(url_for('home', _external=True) + "topics/computer-setup/software-installation/python/python-packages/", code=301)

    @app.route('/building-blocks/configure-your-computer/statistics-and-computation/perl/')
    def redirect_421():
        return redirect(url_for('home', _external=True) + "topics/computer-setup/software-installation/perl/perl/", code=301)

    @app.route('/tutorials/more-tutorials/openai-whisper/whisper')
    def redirect_422():
        return redirect(url_for('home', _external=True) + "topics/automation/ai/transcription/whisper/", code=301)

    @app.route('/building-blocks/configure-your-computer/automation-and-workflows/make/')
    def redirect_423():
        return redirect(url_for('home', _external=True) + "topics/automation/automation-tools/makefiles/make/", code=301)

    @app.route('/building-blocks/analyze-data/regressions-paneldata/impact-evaluation/')
    def redirect_424():
        return redirect(url_for('home', _external=True) + "topics/analyze/causal-inference/did/impact-evaluation/", code=301)

    @app.route('/building-blocks/analyze-data/regressions-paneldata/fixest/')
    def redirect_425():
        return redirect(url_for('home', _external=True) + "topics/analyze/causal-inference/panel-data/fixest/ ", code=301)

    @app.route('/building-blocks/automate-and-execute-your-work/reproducible-work/google_cloud_docker/')
    def redirect_426():
        return redirect(url_for('home', _external=True) + "topics/automation/replicability/cloud-computing/google_cloud_docker/ ", code=301)

    @app.route('/building-blocks/configure-your-computer/statistics-and-computation/r/ ')
    def redirect_427():
        return redirect(url_for('home', _external=True) + "topics/computer-setup/software-installation/rstudio/r/ ", code=301)

    @app.route('/building-blocks/configure-your-computer/statistics-and-computation/python/ ')
    def redirect_428():
        return redirect(url_for('home', _external=True) + "topics/computer-setup/software-installation/python/python/ ", code=301)

    @app.route('/building-blocks/analyze-data/regression-discontinuity/rd-plots/')
    def redirect_429():
        return redirect(url_for('home', _external=True) + "topics/analyze/causal-inference/rdd/rd-plots/", code=301)

    @app.route('/topics/collaborate-share/project-management/engage-open-science/contribute-to-tilburg-science-hub/tutorial-shell/')
    def redirect_430():
        return redirect(url_for('home', _external=True) + "topics/collaborate-share/project-management/contribute-to-tilburg-science-hub/tutorial-shell/", code=301)
   
    @app.route('/topics/collaborate-share/project-management/engage-open-science/contribute-to-tilburg-science-hub/pullrequests/')
    def redirect_431():
        return redirect(url_for('home', _external=True) + "/topics/collaborate-share/project-management/contribute-to-tilburg-science-hub/pullrequests/", code=301)
    
    @app.route('/building-blocks/analyze-data/regressions/survival-analysis-lubridate/')
    def redirect_432():
        return redirect(url_for('home', _external=True) + "topics/analyze/regression/linear-regression/survival-analysis-lubridate/", code=301)
    
    @app.route('/building-blocks/')
    def redirect_433():
        return redirect(url_for('home', _external=True) + "topics/", code=301)
    