import "./DashboardCards.css";

function DashboardCards({ summary }) {

  const cards = [
    {
      title: "Total Products",
      value: summary.total_products,
      icon: "📦",
      className: "products"
    },
    {
      title: "High Risk",
      value: summary.high_risk,
      icon: "🔴",
      className: "high"
    },
    {
      title: "Medium Risk",
      value: summary.medium_risk,
      icon: "🟠",
      className: "medium"
    },
    {
      title: "Low Risk",
      value: summary.low_risk,
      icon: "🟢",
      className: "low"
    }
  ];

  return (
    <section className="dashboard-cards">

      {cards.map((card) => (
        <div
          key={card.title}
          className={`dashboard-card ${card.className}`}
        >

          <div className="card-top">

            <span className="card-icon">
              {card.icon}
            </span>

            <span className="card-title">
              {card.title}
            </span>

          </div>

          <h2 className="card-value">
            {card.value}
          </h2>

        </div>
      ))}

    </section>
  );
}

export default DashboardCards;