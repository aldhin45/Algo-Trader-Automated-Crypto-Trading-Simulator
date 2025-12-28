import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import os

# KONFIGURASI 
ASSET = "BTC-USD"       # Aset bisa diganti
START_DATE = "2023-01-01"
END_DATE = "2024-12-30"
INITIAL_CAPITAL = 10000000 

def run_backtest():
    print(f"📥 Mengambil data {ASSET} dari Yahoo Finance...")
    df = yf.download(ASSET, start=START_DATE, end=END_DATE)
    
    if df.empty:
        print("Data tidak ditemukan!")
        return

    # Hitung Indikator
    df['SMA_20'] = df['Close'].rolling(window=20).mean()
    df['SMA_50'] = df['Close'].rolling(window=50).mean()

    # Logika trading
    cash = INITIAL_CAPITAL
    holdings = 0
    in_position = False
    trade_history = []

    print("🤖 Memulai Simulasi Trading...")
    
    for i in range(50, len(df)):
        price = float(df['Close'].iloc[i])
        date = df.index[i]
        
        sma20_now = df['SMA_20'].iloc[i]
        sma50_now = df['SMA_50'].iloc[i]
        sma20_prev = df['SMA_20'].iloc[i-1]
        sma50_prev = df['SMA_50'].iloc[i-1]

        if sma20_now > sma50_now and sma20_prev < sma50_prev and not in_position:
            holdings = cash / price
            cash = 0
            in_position = True
            trade_history.append((date, price, 'BUY'))

        elif sma20_now < sma50_now and sma20_prev > sma50_prev and in_position:
            cash = holdings * price
            holdings = 0
            in_position = False
            trade_history.append((date, price, 'SELL'))

    # Hitung Hasil Akhir
    final_value = cash
    if in_position:
        last_price = df['Close'].iloc[-1]
        if hasattr(last_price, 'item'): last_price = last_price.item()
        final_value = holdings * last_price
    
    final_value = float(final_value)
    profit = final_value - INITIAL_CAPITAL
    roi = (profit / INITIAL_CAPITAL) * 100

    # Print Laporan di Terminal
    print("\n" + "="*40)
    print(f"HASIL AKHIR TRADING BOT ({ASSET})")
    print("="*40)
    print(f"Total Profit    : Rp {profit:,.0f} ({roi:.2f}%)")
    print("="*40)

    # --- VISUALISASI & PENYIMPANAN GAMBAR ---
    plt.figure(figsize=(15, 8)) # Ukuran sedikit lebih besar agar jelas
    plt.plot(df.index, df['Close'], label='Harga Pasar', alpha=0.4, color='gray')
    plt.plot(df.index, df['SMA_20'], label='SMA 20 (Cepat)', color='orange', linewidth=1.5)
    plt.plot(df.index, df['SMA_50'], label='SMA 50 (Lambat)', color='blue', linewidth=1.5)

    # Plot titik beli/jual
    for date, price, action in trade_history:
        color = 'green' if action == 'BUY' else 'red'
        marker = '^' if action == 'BUY' else 'v'
        plt.scatter(date, price, color=color, marker=marker, s=150, zorder=5, label=action if action not in [l.get_label() for l in plt.gca().get_lines()] else "")

    plt.title(f'Analysis Report: {ASSET} Strategy Portfolio', fontsize=16)
    plt.xlabel('Tanggal', fontsize=12)
    plt.ylabel('Harga (USD)', fontsize=12)
    plt.legend(loc='best')
    plt.grid(True, alpha=0.3)
    
    # Menambahkan teks ringkasan di dalam grafik (Opsional tapi keren)
    info_text = f'Initial: Rp {INITIAL_CAPITAL:,.0f}\nFinal: Rp {final_value:,.0f}\nROI: {roi:.2f}%'
    plt.gca().text(0.02, 0.95, info_text, transform=plt.gca().transAxes, fontsize=12,
            verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.5))

    # --- SIMPAN GAMBAR DISINI ---
    filename = f"trading_report_{ASSET}.png"
    plt.savefig(filename, dpi=300, bbox_inches='tight') # dpi=300 untuk kualitas tinggi (HD)
    print(f"✅ Grafik berhasil disimpan sebagai: {filename}")
    
    plt.show()

if __name__ == "__main__":
    run_backtest()