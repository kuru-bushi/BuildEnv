
    function createTable(containerId, headers, rows) {
      const container = document.getElementById(containerId);

      const table = document.createElement('table');
      // ヘッダー行の作成
      const thead = document.createElement('thead');
      const trHead = document.createElement('tr');
      headers.forEach(text => {
        const th = document.createElement('th');
        th.textContent = text;
        trHead.appendChild(th);
      });
      thead.appendChild(trHead);
      table.appendChild(thead);

      // データ行の作成
      const tbody = document.createElement('tbody');
      rows.forEach(rowData => {
        const tr = document.createElement('tr');
        rowData.forEach(text => {
          const td = document.createElement('td');
          td.textContent = text;
          tr.appendChild(td);
        });
        tbody.appendChild(tr);
      });
      table.appendChild(tbody);

      container.appendChild(table);
    }
