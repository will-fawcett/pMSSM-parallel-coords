# pMSSM parallel coordinates
- Contained in this repository is sufficient code to re-create the webpage hosted here: http://www-pnp.physics.ox.ac.uk/~fawcett/pmssm.html
- The code makes heavy use of the open-source D3 software: https://d3js.org/, which is excellent for displaying data in visually impressive formats.

## Information about what is on the website
- The webpage displays a parallel coordinates plot of several points in the phenomenological minimal supersymmetric extension to the standard model (pMSSM) parameter space that were selected for this paper, [JHEP 10 (2015) 134](http://link.springer.com/article/10.1007%2FJHEP10%282015%29134) wherein more information about the pMSSM can be found, the important thing is the pMSSM is a 19 parameter space.
- Each line on the plot corresponds to a point in this 19 dimensional space, and represents a different theoretical model of beyond-the-standard model physics.
- Each axis on the plot corresponds to either one of these 19 parameters, or some other calculable observable about the theory that is of some physical interest. 
- Each "point", or line on the plot, corresponds to a different new-physics theory.
- The colour of each line corresponds to the composition of the lightest supersymmetric particle (LSP) in the theory, which is of particular phenomenological importance.
- Red, blue and green correspond to a LSP that is mostly bino, wino or higgsino in composition, again see the paper for details. 

## Some technical details 
- The information for each point is stored in `pmssm_10.csv`. The first line of this file contains column headings (each corresponding to an axis), and all subsequent lines correspond to a point in the pMSSM. 
- Not all of the information in the .csv file is drawn on the plot, and this can be configured by the user. 
- The CSV file is parsed by `parallel.js`, and the list of axes is selected by filling in the `vars` list from the set present in `pmssm_10.csv`
