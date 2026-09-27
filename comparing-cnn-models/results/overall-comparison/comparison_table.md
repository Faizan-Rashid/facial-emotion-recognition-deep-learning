# CNN Model Comparison Table

<div style="text-align: right; margin-bottom: 20px;">
  <button onclick="toggleFullscreen()" style="padding: 8px 16px; background-color: #007bff; color: white; border: none; border-radius: 4px; cursor: pointer; font-size: 14px;">
    🖥️ Toggle Fullscreen
  </button>
</div>

<div id="tableContainer" style="overflow-x: auto; border: 1px solid #ddd; border-radius: 4px;">

| index | model              | Architecture | accuracy            | loss                | FLOPS          | MACs          | Size (Parameters) | Confusion Matrix                                                          |
| ----- | ------------------ | ------------ | ------------------- | ------------------- | -------------- | ------------- | ------------------- | ------------------------------------------------------------------------- |
| 0     | mobilenet_v3_small | MobileNetV3  | 0.7091111730286987 | 0.9051066817177666 | 114.6 MFLOPS  | 55.49 MMACs  | 1.53 M             | ![alt text](../confusion-matrices/mobilenet_v3_small/by-sample-count.png) |
| 1     | shufflenet_v2_x0_5 | ShuffleNetV2 | 0.6829200334354973 | 0.8954495419396294 | 82.09 MFLOPS  | 39.46 MMACs  | 348.97 K           | ![alt text](../confusion-matrices/shufflenet_v2_x0_5/by-sample-count.png) |
| 2     | shufflenet_v2_x1_0 | ShuffleNetV2 | 0.7035385901365283 | 0.8951992658774058 | 293.47 MFLOPS | 143.89 MMACs | 1.26 M             | ![alt text](../confusion-matrices/shufflenet_v2_x1_0/by-sample-count.png) |
| 3     | efficientnet_b0    | EfficientNet | 0.7070214544441349 | 0.9830353075928159 | 791.1 MFLOPS  | 384.54 MMACs | 4.02 M             | ![alt text](../confusion-matrices/efficientnet_b0/by-sample-count.png)    |
| 4     | efficientnet_b1    | EfficientNet | 0.7238785176929506 | 0.8524766141838498 | 1.17 GFLOPS   | 568.38 MMACs | 6.52 M             | ![alt text](../confusion-matrices/efficientnet_b1/by-sample-count.png)    |

</div>

<style>
  #tableContainer {
    transition: all 0.3s ease;
    max-height: 600px;
  }
  
  #tableContainer.fullscreen {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 9999;
    max-height: 100%;
    border-radius: 0;
    background-color: white;
    padding: 60px 20px 20px 20px;
    overflow: auto;
  }
  
  #tableContainer table {
    font-size: 14px;
    width: 100%;
    border-collapse: collapse;
  }
  
  #tableContainer.fullscreen table {
    font-size: 16px;
  }
  
  #tableContainer table th,
  #tableContainer table td {
    padding: 12px;
    text-align: left;
    border: 1px solid #ddd;
  }
  
  #tableContainer table th {
    background-color: #f8f9fa;
    font-weight: bold;
  }
  
  #tableContainer table tr:hover {
    background-color: #f5f5f5;
  }
  
  body.fullscreen-mode {
    overflow: hidden;
  }
</style>

<script>
  function toggleFullscreen() {
    const container = document.getElementById('tableContainer');
    const body = document.body;
    
    container.classList.toggle('fullscreen');
    body.classList.toggle('fullscreen-mode');
    
    const button = event.target;
    if (container.classList.contains('fullscreen')) {
      button.textContent = '✕ Exit Fullscreen';
      button.style.position = 'fixed';
      button.style.top = '10px';
      button.style.right = '10px';
      button.style.zIndex = '10000';
    } else {
      button.textContent = '🖥️ Toggle Fullscreen';
      button.style.position = 'static';
    }
  }
</script>

## Model Performance Summary

- **Best Accuracy**: EfficientNetB1 (0.7239)
- **Smallest Model**: ShuffleNetV2 X0.5 (348.97 K parameters)
- **Most Efficient**: MobileNetV3 Small (114.6 MFLOPS, 1.53 M parameters)
- **Best FLOPS/Accuracy Ratio**: ShuffleNetV2 X0.5
