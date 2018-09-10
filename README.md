# SugarTeX Completions for Atom

Easy Unicode input for Atom optimized for [SugarTeX](https://github.com/kiwi0fruit/sugartex).

It's simple enough – SugarTeX Completions takes LaTeX character names such as
`\alpha` and replaces them with unicode characters like `α`.

It also supports easy SugarTeX input with object transform oriented typing. SugarTeX Completions for Atom main goal is to provide fast input for [SugarTeX](https://github.com/kiwi0fruit/sugartex) that is a more readable LaTeX language extension and transcompiler to LaTeX.

**Documentation**: in the [SugarTeX documentation](https://github.com/kiwi0fruit/sugartex/blob/master/sugartex.md) appropriate shortcuts for SugarTeX Completions for Atom are given. But SugarTeX Completions for Atom has even more shortcuts! They all are intuitive for remembering and typing: simply think of the way the symbol can be obtained from standard characters via transformations:

* Transformations are invoked via typing `\` **after** object like `\->\rot` gives `↑` (rotated). First `\` starts SugarTeX Completions,
* Making superscript and subscript are special transformations that are used like functions instead of methods: `\^1` to `¹`, `\_1` to `₁`. Many other objects moved up/down and resized like `\^o\degree` to `°`,
* Combining superscript and subscripts symbols are typed with `^^`/`__` like `\^^'`/`\__'` (accentuation).
* Combining overlay symbols are typed with `@` like `\@/` or `\@-` (strikethrough).
* See the list of the shortcuts in [this file](https://github.com/kiwi0fruit/sugartex-completions/blob/master/completions/completions.json).

**Warning**: incompatible with [latex-completions](https://atom.io/packages/latex-completions) - uninstall it first if installed.

<div align="center"><img src="https://raw.githubusercontent.com/kiwi0fruit/atom-sugartex-completions/master/demo.gif" /></div>
