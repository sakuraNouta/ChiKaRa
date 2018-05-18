import pandas as pd

budget = pd.read_csv("b.csv")
print(budget)
budget = budget.sort_values('amount',ascending=False)[:10]

#print(budget)

#pd.set_option('display.mpl_style', 'default')
budget_plot = budget.plot(kind="bar",x=budget["detail"],
                          title="MN Capital Budget - 2014",
                          legend=False)
fig = budget_plot.get_figure()
fig.show()
#fig.savefig("a.png")
