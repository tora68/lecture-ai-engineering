import pandas as pd
import streamlit as st
from database import get_chat_history

def download_csv_from_db():
    """データベースから取得した履歴データをCSVとしてダウンロードする"""
    # データベースから履歴データを取得
    history_df = get_chat_history()

    if history_df.empty:
        st.info("データベースに履歴データがありません。")
        return

    # CSV形式でデータをエクスポート
    csv_data = history_df.to_csv(index=False)

    # ダウンロードボタンを表示
    st.download_button(
        label="CSVとしてダウンロード",
        data=csv_data,
        file_name="chat_history.csv",
        mime="text/csv"
    )

def display_csv_download_section():
    """CSVダウンロードセクションの表示"""
    st.header("チャット履歴 CSV ダウンロード")
    download_csv_from_db()
