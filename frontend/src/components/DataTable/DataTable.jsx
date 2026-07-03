import "./DataTable.css";

function DataTable({ data, search,setSearch}) {

  return (
    <section className="table-card">

      <div className="table-header">

        <div className="table-title">

        <div>
        <h2>Inventory Records</h2>

        <p>
          Uploaded inventory dataset and prediction results.
        </p>
       </div>

         <input
           type="text"
           placeholder="🔍 Search by Product ID or Product Name..."
           value={search}
          onChange={(e) => setSearch(e.target.value)}
          className="search-input"
         />

        </div>

      </div>
      

      <div className="table-container">

        <table>

          <thead>

            <tr>

              <th>Product ID</th>

              <th>Product</th>

              <th>Stock</th>

              <th>Forecast</th>

              <th>Days Left</th>

              <th>Risk</th>

              <th>Action</th>

            </tr>

          </thead>

          <tbody>

            {data.length === 0 ? (

              <tr>

                <td
                  colSpan="7"
                  className="empty-table"
                >
                  Upload a CSV file to view inventory data.
                </td>

              </tr>

            ) : (

              data.map((row) => (

                <tr key={row.product_id}>

                  <td>{row.product_id}</td>

                  <td>{row.product_name}</td>

                  <td>{row.stock}</td>

                  <td>{row.predicted_sales}</td>

                  <td>{row.days_left}</td>

                  <td>

                    <span
                      className={`risk-badge ${row.risk.toLowerCase()}`}
                    >
                      {row.risk}
                    </span>

                  </td>

                  <td>

                    <span
                      className={`action-badge ${row.action
                        .toLowerCase()
                        .replace(/\s+/g, "-")}`}
                    >
                      {row.action}
                    </span>

                  </td>

                </tr>

              ))

            )}

          </tbody>

        </table>

      </div>

    </section>
  );
}

export default DataTable;