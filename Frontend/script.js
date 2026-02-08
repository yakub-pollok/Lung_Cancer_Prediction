function predict() {
    const data = {
        GENDER: Number(GENDER.value),
        AGE: Number(AGE.value),
        SMOKING: Number(SMOKING.value),
        YELLOW_FINGERS: Number(YELLOW_FINGERS.value),
        ANXIETY: Number(ANXIETY.value),
        PEER_PRESSURE: Number(PEER_PRESSURE.value),
        CHRONIC_DISEASE: Number(CHRONIC_DISEASE.value),
        FATIGUE: Number(FATIGUE.value),
        ALLERGY: Number(ALLERGY.value),
        WHEEZING: Number(WHEEZING.value),
        ALCOHOL_CONSUMING: Number(ALCOHOL_CONSUMING.value),
        COUGHING: Number(COUGHING.value),
        SHORTNESS_OF_BREATH: Number(SHORTNESS_OF_BREATH.value),
        SWALLOWING_DIFFICULTY: Number(SWALLOWING_DIFFICULTY.value),
        CHEST_PAIN: Number(CHEST_PAIN.value)
    };

    fetch("https://lung-cancer-prediction-fxg7.onrender.com/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(result => {
        document.getElementById("result").innerText = result.result;
    })
    .catch(err => {
        alert("API Error");
        console.error(err);
    });
}
