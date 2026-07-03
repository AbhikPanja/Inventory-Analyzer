import { useState } from "react";
import Header from "../components/Header/Header";
import DashboardCards from "../components/DashboardCards/DashboardCards";
import CsvUploader from "../components/CsvUploader/CsvUploader";
import DataTable from "../components/DataTable/DataTable";
import ChatbotPanel from "../components/Chatbot/ChatbotPanel";
function Home() {

  const [summary, setSummary] = useState({
    total_products: 0,
    high_risk: 0,
    medium_risk: 0,
    low_risk: 0
  });

  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(false);
  
  const [search, setSearch] = useState("");

  const filteredData = data.filter((item) => {
  const text = search.trim().toLowerCase();

    return (
      item.product_id?.toString().toLowerCase().includes(text) ||
      item.product_name?.toLowerCase().includes(text)
    );
  });
  

  return (
    <main className="dashboard-content">
      <Header />
      <DashboardCards summary={summary} />
      <CsvUploader
       setData={setData}
       setSummary={setSummary}
       loading={loading}
       setLoading={setLoading}
      />
      <DataTable
       data={filteredData}
       search={search}
       setSearch={setSearch}
    />
      <ChatbotPanel />
    </main>
  );
}

export default Home;