# SARIMA vs Prophet Premium
fig, ax = plt.subplots(figsize=(16, 8))
fig.patch.set_facecolor('#F8F9FA')
ax.set_facecolor('#F8F9FA')

# Train
ax.plot(train.index, train.values,
        color='#CCCCCC', linewidth=1.2, alpha=0.8, label='Train')

# Zona e testit
ax.axvspan(test.index[0], test.index[-1],
           alpha=0.06, color='#1D9E75')

# Aktual
ax.plot(test.index, test.values,
        color='#1D9E75', linewidth=3,
        marker='o', markersize=8,
        zorder=5, label='Aktual (Test)')

# SARIMA
ax.plot(test.index, preds,
        color='#E24B4A', linewidth=2.5,
        linestyle='--', marker='s', markersize=6,
        zorder=4, label=f'SARIMA  MAE={mae:.1f}  RMSE={rmse:.1f}')

# Prophet
ax.plot(test.index, preds_p,
        color='#534AB7', linewidth=2.5,
        linestyle='--', marker='^', markersize=6,
        zorder=4, label=f'Prophet  MAE={mae_p:.1f}  RMSE={rmse_p:.1f}')

# Vija ndarëse
ax.axvline(test.index[0], color='gray',
           linestyle=':', linewidth=1.5)
ax.text(test.index[0], ax.get_ylim()[0] + 5,
        ' Test fillon', color='gray', fontsize=9)

# Badge fituesi
winner = 'SARIMA' if mae < mae_p else 'Prophet'
winner_mae = mae if mae < mae_p else mae_p
ax.text(0.98, 0.95, f'Fituesi: {winner}\nMAE={winner_mae:.1f}',
        transform=ax.transAxes, fontsize=11,
        fontweight='bold', color='#1D9E75',
        ha='right', va='top',
        bbox=dict(boxstyle='round,pad=0.5',
                 facecolor='white',
                 edgecolor='#1D9E75',
                 linewidth=2, alpha=0.9))

# Shto vlerat aktuale vs parashikim
for i, (t, a, s, p) in enumerate(zip(test.index, test.values, preds, preds_p)):
    ax.annotate(f'{a:.0f}', (t, a),
                textcoords='offset points',
                xytext=(0, 10), fontsize=8,
                color='#1D9E75', fontweight='bold',
                ha='center')

ax.set_ylabel('Numri i krimeve', fontsize=12)
ax.set_xlabel('')
ax.set_title('SARIMA vs Prophet — Other Theft Forecasting\nCity of London (2023–2026)',
             fontsize=14, fontweight='bold', pad=15)
ax.legend(fontsize=10, loc='upper left',
          framealpha=0.9, edgecolor='white')
ax.grid(True, alpha=0.3, linestyle='--', color='white')
sns.despine()
plt.tight_layout()
plt.savefig('comparison.png', dpi=150, bbox_inches='tight')
plt.show()
print("✅ Krahasimi Premium u ruajt!")
print(f"\n=== KRAHASIMI FINAL ===")
print(f"{'Model':<10} {'MAE':>8} {'RMSE':>8} {'Fituesi':>10}")
print("-" * 42)
print(f"{'SARIMA':<10} {mae:>8.1f} {rmse:>8.1f} {'✅' if mae < mae_p else '':>10}")
print(f"{'Prophet':<10} {mae_p:>8.1f} {rmse_p:>8.1f} {'✅' if mae_p < mae else '':>10}")
print("-" * 42)
print(f"Modeli më i mirë: {winner}!")