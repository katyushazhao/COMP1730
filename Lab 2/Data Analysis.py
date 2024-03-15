population = 196037
families = 50352
couple_with_children = 22850
single_parent = 7243
childless_couples=families-(couple_with_children+single_parent)
children=(couple_with_children+single_parent)*1.8
non_single_adults=(childless_couples*2)+(couple_with_children*2)
single_adults=round(population-(non_single_adults+children),0)
print("Single Adults: ",single_adults)
