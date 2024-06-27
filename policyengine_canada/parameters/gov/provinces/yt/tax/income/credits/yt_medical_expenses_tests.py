- name: Yukon medical expense credit net income below reduction cap 2022
  period: 2022
  input:
    people:
      p1:
        individual_net_income: 10_000
    household:
      members: p1
      province_code: YT
  output:
    yt_medical_expense_credit: 300  # 10_000 * 0.03

- name: Yukon medical expense credit zero net income 2022
  period: 2022
  input:
    people:
      p1:
        individual_net_income: 0
    household:
      members: p1
      province_code: YT
  output:
    yt_medical_expense_credit: 0

- name: Yukon medical expense credit net income below reduction cap 2023
  period: 2023
  input:
    people:
      p1:
        individual_net_income: 20_000
    household:
      members: p1
      province_code: YT
  output:
    yt_medical_expense_credit: 600  # 20_000 * 0.03