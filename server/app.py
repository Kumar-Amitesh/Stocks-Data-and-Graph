from flask import Flask, jsonify, request
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def load_and_preprocess_data():
    df = pd.read_csv("D:/Web/stocks/dump.csv")
    
    mean_values = df.mean(numeric_only=True)

    df.fillna(mean_values, inplace=True)
    

    df["index_date"] = pd.to_datetime(df["index_date"], errors="coerce")
    df["index_date"] = df["index_date"].ffill()  
    df["index_date"] = df["index_date"].bfill()   

    df.sort_values("index_date", ascending=False, inplace=True)

    
    required_columns = ["index_date", "index_name", "open_index_value", "high_index_value", 
                        "low_index_value", "closing_index_value", "volume"]
    
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing required column in CSV: {col}")
    
    return df


@app.route("/api/indexes", methods=["GET"])
def get_indexes():
    data = load_and_preprocess_data()
    indexes = data["index_name"].unique().tolist()
    return jsonify(indexes)


@app.route("/api/data", methods=["GET"])
def get_data():
    index_name = request.args.get("index")
    if not index_name:
        return jsonify({"error": "Index name is required"}), 400
    
    data = load_and_preprocess_data()
    filtered = data[data["index_name"] == index_name]
    # print(len(filtered))
    
    if filtered.empty:
        return jsonify({"error": "No data found for this index"}), 404


    response = {
        "dates": filtered["index_date"].astype(str).tolist(),
        "open": filtered["open_index_value"].fillna(0).tolist(),
        "high": filtered["high_index_value"].fillna(0).tolist(),
        "low": filtered["low_index_value"].fillna(0).tolist(),
        "close": filtered["closing_index_value"].fillna(0).tolist(),
        "points_change": filtered["points_change"].fillna(0).tolist(),
        "change_percent": filtered["change_percent"].fillna(0).tolist(),
        "volume": filtered["volume"].fillna(0).tolist(),
        "turnover_rs_cr": filtered["turnover_rs_cr"].fillna(0).tolist(),
        "pe_ratio": filtered["pe_ratio"].fillna(0).tolist(),
        "pb_ratio": filtered["pb_ratio"].fillna(0).tolist(),
        "div_yield": filtered["div_yield"].fillna(0).tolist(),
        "table_data": filtered.rename(columns={"index_date": "Date", 
                                            "open_index_value": "Open", 
                                            "high_index_value": "High", 
                                            "low_index_value": "Low", 
                                            "closing_index_value": "Close"}).fillna(0).to_dict(orient="records")
    }


    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
