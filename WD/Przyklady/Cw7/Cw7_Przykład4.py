# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

fig = plt.figure()
#Tworzymy tytuł
fig.suptitle('Tytuł główny rysunku', fontsize=14, fontweight='bold')

ax = fig.add_subplot(111)
fig.subplots_adjust(top=0.85)
ax.set_title('podtytuł rysunku')

ax.set_xlabel('oś x')
ax.set_ylabel('oś y')

ax.text(3, 8, 'Italiki zapisane w ramce', style='italic',
        bbox={'facecolor':'green', 'alpha':0.5, 'pad':15})

ax.text(2, 6, r'Możemy pisać równania w stylu texowym: $\sum_{i=1}^{\infty}=\frac{1}{i^2}$', fontsize=10)

ax.text(2, 5, u' i po polsku: Zażółć gęślą jaźń')

ax.text(0.3, 0.02, 'różowy tekst',
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='pink', fontsize=15)


ax.plot([2], [1], 'o')
ax.annotate('Wskazuje na', xy=(2, 1), xytext=(3, 4),
            arrowprops=dict(facecolor='black', shrink=0.05))

ax.axis([0, 10, 0, 10])

plt.show()
