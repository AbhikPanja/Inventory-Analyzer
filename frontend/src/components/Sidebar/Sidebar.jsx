import "./Sidebar.css";

function Sidebar() {
  return (
    <aside className="sidebar">

      <div className="sidebar-logo">

        <h2>📦 Inventory AI</h2>

        <p>Smart Analytics</p>

      </div>

      <nav>

        <button className="sidebar-item active">
          📊 Dashboard
        </button>

        <button className="sidebar-item">
          📁 Upload Data
        </button>

        <button className="sidebar-item">
          📈 Forecast Analysis
        </button>

        <button className="sidebar-item">
          ⚠ Risk Analysis
        </button>

        <button className="sidebar-item">
          📋 Results
        </button>

        <button className="sidebar-item">
          🤖 AI Assistant
        </button>

      </nav>

    </aside>
  );
}

export default Sidebar;